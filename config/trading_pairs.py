# 交易对配置 - 前十大加密货币
# 支持 Bitget 和 OKX 交易所

TOP_10_TRADING_PAIRS = {
    'bitget': [
        'BTC-USDT',   # Bitcoin - 市值第一
        'ETH-USDT',   # Ethereum - 市值第二
        'BNB-USDT',   # Binance Coin
        'SOL-USDT',   # Solana
        'XRP-USDT',   # Ripple
        'ADA-USDT',   # Cardano
        'DOGE-USDT',  # Dogecoin
        'AVAX-USDT',  # Avalanche
        'DOT-USDT',   # Polkadot
        'MATIC-USDT'  # Polygon
    ],
    'okx': [
        'BTC-USDT',
        'ETH-USDT',
        'BNB-USDT',
        'SOL-USDT',
        'XRP-USDT',
        'ADA-USDT',
        'DOGE-USDT',
        'AVAX-USDT',
        'DOT-USDT',
        'MATIC-USDT'
    ]
}

# 时间框架配置
TIMEFRAMES = ['1m', '5m', '15m', '1h', '4h', '1D']

# 回测配置
BACKTEST_CONFIG = {
    'starting_balance': 10000,  # USDT
    'fee': 0.001,  # 0.1% 手续费
    'futures_leverage': 3,  # 3x 杠杆
    'futures_leverage_mode': 'cross',  # 全仓模式
}

# 实盘交易配置
LIVE_CONFIG = {
    'symbols': TOP_10_TRADING_PAIRS,
    'warmup_candles': 100,  # 预热蜡烛数量
    'exchange': 'Bitget Futures',  # 默认交易所
}
