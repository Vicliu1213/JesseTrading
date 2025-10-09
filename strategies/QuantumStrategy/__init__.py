from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.bitget_config import BitgetConfig

class QuantumStrategy(Strategy):
    """
    量子增强交易策略 - 整合前十大加密货币
    支持 Bitget 和 OKX 交易所
    """
    
    # 前十大加密货币配置
    TOP_10_CRYPTOS = [
        'BTC-USDT',  # Bitcoin
        'ETH-USDT',  # Ethereum
        'BNB-USDT',  # Binance Coin
        'SOL-USDT',  # Solana
        'XRP-USDT',  # Ripple
        'ADA-USDT',  # Cardano
        'DOGE-USDT', # Dogecoin
        'AVAX-USDT', # Avalanche
        'DOT-USDT',  # Polkadot
        'MATIC-USDT' # Polygon
    ]
    
    def __init__(self):
        super().__init__()
        self.vars['entry_price'] = None
        self.vars['position_size'] = 0
    
    def should_long(self) -> bool:
        """
        做多信号判断
        """
        # 双均线策略
        short_ema = ta.ema(self.candles, 20)
        long_ema = ta.ema(self.candles, 50)
        
        # RSI 指标
        rsi = ta.rsi(self.candles, 14)
        
        # 做多条件：短期均线上穿长期均线 且 RSI 低于 70
        if short_ema > long_ema and rsi < 70:
            return True
        
        return False
    
    def should_short(self) -> bool:
        """
        做空信号判断
        """
        # 双均线策略
        short_ema = ta.ema(self.candles, 20)
        long_ema = ta.ema(self.candles, 50)
        
        # RSI 指标
        rsi = ta.rsi(self.candles, 14)
        
        # 做空条件：短期均线下穿长期均线 且 RSI 高于 30
        if short_ema < long_ema and rsi > 30:
            return True
        
        return False
    
    def should_cancel_entry(self) -> bool:
        return False
    
    def go_long(self):
        """
        执行做多
        """
        qty = self.calculate_position_size()
        self.buy = qty, self.price
        self.vars['entry_price'] = self.price
        self.vars['position_size'] = qty
        
        # 设置止损和止盈
        self.stop_loss = qty, self.price * 0.98  # 2% 止损
        self.take_profit = qty, self.price * 1.05  # 5% 止盈
    
    def go_short(self):
        """
        执行做空
        """
        qty = self.calculate_position_size()
        self.sell = qty, self.price
        self.vars['entry_price'] = self.price
        self.vars['position_size'] = qty
        
        # 设置止损和止盈
        self.stop_loss = qty, self.price * 1.02  # 2% 止损
        self.take_profit = qty, self.price * 0.95  # 5% 止盈
    
    def calculate_position_size(self):
        """
        计算仓位大小（风险管理）- Bitget 优化版
        """
        # 获取 Bitget 交易对配置
        pair_config = BitgetConfig.get_pair_config(self.symbol)
        min_order_size = pair_config['min_order_size']
        
        # 使用账户资金的 1% 作为每笔交易的风险
        risk_per_trade = self.capital * 0.01
        
        # 基于止损距离计算仓位
        stop_loss_distance = self.price * 0.02  # 2% 止损
        calculated_qty = risk_per_trade / stop_loss_distance
        
        # 确保满足 Bitget 最小订单要求
        qty = max(calculated_qty, min_order_size)
        
        # 根据 Bitget 精度要求调整
        precision = pair_config['precision']
        qty = round(qty, precision)
        
        return qty
    
    def update_position(self):
        """
        更新持仓（追踪止损等）
        """
        if self.is_long:
            # 移动止损（盈利后）
            if self.price > self.vars['entry_price'] * 1.03:
                self.stop_loss = self.position.qty, self.vars['entry_price'] * 1.01
        
        elif self.is_short:
            # 移动止损（盈利后）
            if self.price < self.vars['entry_price'] * 0.97:
                self.stop_loss = self.position.qty, self.vars['entry_price'] * 0.99
    
    @property
    def short_ema(self):
        return ta.ema(self.candles, 20)
    
    @property
    def long_ema(self):
        return ta.ema(self.candles, 50)
    
    @property
    def rsi_value(self):
        return ta.rsi(self.candles, 14)
    
    def _as_scalar(self, value):
        """将指标值转换为标量（处理 ndarray 类型）"""
        if hasattr(value, '__len__'):
            return float(value[-1])
        return float(value)
    
    def watch_list(self):
        """
        监控列表 - 实时显示在仪表板
        """
        return [
            ('Symbol', self.symbol),
            ('Price', self.price),
            ('Short EMA', round(self._as_scalar(self.short_ema), 2)),
            ('Long EMA', round(self._as_scalar(self.long_ema), 2)),
            ('RSI', round(self._as_scalar(self.rsi_value), 2)),
            ('Position', 'Long' if self.is_long else 'Short' if self.is_short else 'None'),
            ('Entry Price', self.vars.get('entry_price', 0)),
            ('PnL', round(self.position.pnl if self.position else 0, 2))
        ]
