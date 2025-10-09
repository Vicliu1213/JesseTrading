
# Bitget 交易所配置
import os
from typing import Dict, List

class BitgetConfig:
    """Bitget 交易所配置类"""
    
    # Bitget 支持的交易对
    SUPPORTED_PAIRS = [
        'BTC/USDT',
        'ETH/USDT', 
        'BNB/USDT',
        'SOL/USDT',
        'XRP/USDT',
        'ADA/USDT',
        'DOGE/USDT',
        'AVAX/USDT',
        'DOT/USDT',
        'MATIC/USDT',
        'LTC/USDT',
        'LINK/USDT',
        'UNI/USDT',
        'ATOM/USDT',
        'FIL/USDT'
    ]
    
    # Bitget API 配置
    API_CONFIG = {
        'sandbox': False,  # 生产环境
        'rateLimit': 1200,  # API 请求限制
        'enableRateLimit': True,
        'timeout': 30000,
        'options': {
            'defaultType': 'spot',  # 现货交易
            'adjustForTimeDifference': True
        }
    }
    
    # 交易配置
    TRADING_CONFIG = {
        'min_order_size': {
            'BTC/USDT': 0.001,
            'ETH/USDT': 0.01,
            'BNB/USDT': 0.1,
            'SOL/USDT': 0.1,
            'XRP/USDT': 10.0,
            'ADA/USDT': 10.0,
            'DOGE/USDT': 100.0,
            'AVAX/USDT': 0.1,
            'DOT/USDT': 1.0,
            'MATIC/USDT': 10.0
        },
        'precision': {
            'BTC/USDT': 8,
            'ETH/USDT': 8,
            'BNB/USDT': 8,
            'SOL/USDT': 8,
            'XRP/USDT': 6,
            'ADA/USDT': 6,
            'DOGE/USDT': 6,
            'AVAX/USDT': 8,
            'DOT/USDT': 8,
            'MATIC/USDT': 6
        }
    }
    
    @classmethod
    def get_exchange_config(cls) -> Dict:
        """获取完整的交易所配置"""
        return {
            'name': 'bitget',
            'class': 'ccxt.bitget',
            'fee': 0.001,  # 0.1% 手续费
            'type': 'spot',
            'futures_leverage': 3,
            'futures_leverage_mode': 'cross',
            'api_key': os.getenv('BITGET_API_KEY', ''),
            'secret': os.getenv('BITGET_API_SECRET', ''),
            'password': os.getenv('BITGET_PASSPHRASE', ''),
            **cls.API_CONFIG
        }
    
    @classmethod
    def get_trading_pairs(cls) -> List[str]:
        """获取支持的交易对列表"""
        return cls.SUPPORTED_PAIRS
    
    @classmethod
    def get_pair_config(cls, pair: str) -> Dict:
        """获取特定交易对的配置"""
        return {
            'min_order_size': cls.TRADING_CONFIG['min_order_size'].get(pair, 0.01),
            'precision': cls.TRADING_CONFIG['precision'].get(pair, 8),
            'fee': 0.001
        }

# Bitget Futures 配置
class BitgetFuturesConfig:
    """Bitget 合约交易配置"""
    
    FUTURES_PAIRS = [
        'BTC/USDT:USDT',
        'ETH/USDT:USDT',
        'BNB/USDT:USDT',
        'SOL/USDT:USDT',
        'XRP/USDT:USDT',
        'ADA/USDT:USDT',
        'DOGE/USDT:USDT',
        'AVAX/USDT:USDT',
        'DOT/USDT:USDT',
        'MATIC/USDT:USDT'
    ]
    
    @classmethod
    def get_futures_config(cls) -> Dict:
        """获取合约配置"""
        return {
            'name': 'bitget_futures',
            'class': 'ccxt.bitget',
            'fee': 0.0006,  # 合约手续费 0.06%
            'type': 'swap',
            'futures_leverage': 10,
            'futures_leverage_mode': 'isolated',  # 逐仓模式
            'api_key': os.getenv('BITGET_API_KEY', ''),
            'secret': os.getenv('BITGET_API_SECRET', ''),
            'password': os.getenv('BITGET_PASSPHRASE', ''),
            'sandbox': False,
            'options': {
                'defaultType': 'swap'
            }
        }
