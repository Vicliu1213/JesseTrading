
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bitget API 连接测试脚本
用于测试 Bitget 交易所的 API 连接和功能
"""

import os
import ccxt
import json
from datetime import datetime
from config.bitget_config import BitgetConfig, BitgetFuturesConfig

def test_bitget_connection():
    """测试 Bitget 连接"""
    print("🚀 开始测试 Bitget 连接...")
    
    # 检查环境变量
    api_key = os.getenv('BITGET_API_KEY')
    api_secret = os.getenv('BITGET_API_SECRET') 
    passphrase = os.getenv('BITGET_PASSPHRASE')
    
    if not all([api_key, api_secret, passphrase]):
        print("❌ 缺少 Bitget API 凭据!")
        print("请在 Secrets 中设置:")
        print("- BITGET_API_KEY")
        print("- BITGET_API_SECRET")
        print("- BITGET_PASSPHRASE")
        return False
    
    try:
        # 创建 Bitget 交易所实例
        exchange = ccxt.bitget({
            'apiKey': api_key,
            'secret': api_secret,
            'password': passphrase,
            'sandbox': False,  # 生产环境
            'enableRateLimit': True,
        })
        
        print("✅ Bitget 实例创建成功!")
        
        # 测试连接
        print("📡 测试 API 连接...")
        markets = exchange.load_markets()
        print(f"✅ 成功获取 {len(markets)} 个交易对!")
        
        # 测试账户信息
        print("💰 获取账户信息...")
        balance = exchange.fetch_balance()
        print("✅ 账户信息获取成功!")
        
        # 显示主要余额
        print("\n📊 账户余额:")
        for currency, amount in balance['total'].items():
            if amount > 0:
                print(f"  {currency}: {amount}")
        
        # 测试价格获取
        print("\n📈 测试价格获取...")
        symbols_to_test = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT']
        
        for symbol in symbols_to_test:
            if symbol in markets:
                ticker = exchange.fetch_ticker(symbol)
                print(f"  {symbol}: ${ticker['last']:.2f}")
            else:
                print(f"  {symbol}: 不支持")
        
        print("\n🎉 Bitget 连接测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ Bitget 连接测试失败: {str(e)}")
        return False

def test_bitget_futures():
    """测试 Bitget 合约功能"""
    print("\n🔮 测试 Bitget 合约功能...")
    
    api_key = os.getenv('BITGET_API_KEY')
    api_secret = os.getenv('BITGET_API_SECRET')
    passphrase = os.getenv('BITGET_PASSPHRASE')
    
    if not all([api_key, api_secret, passphrase]):
        print("❌ 缺少 API 凭据!")
        return False
    
    try:
        exchange = ccxt.bitget({
            'apiKey': api_key,
            'secret': api_secret,
            'password': passphrase,
            'sandbox': False,
            'options': {'defaultType': 'swap'},  # 合约模式
        })
        
        # 获取合约市场信息
        markets = exchange.load_markets()
        futures_markets = {k: v for k, v in markets.items() if v['type'] == 'swap'}
        
        print(f"✅ 发现 {len(futures_markets)} 个合约交易对!")
        
        # 测试合约价格
        print("\n📊 合约价格:")
        test_symbols = ['BTC/USDT:USDT', 'ETH/USDT:USDT']
        
        for symbol in test_symbols:
            if symbol in futures_markets:
                ticker = exchange.fetch_ticker(symbol)
                print(f"  {symbol}: ${ticker['last']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ 合约测试失败: {str(e)}")
        return False

def show_bitget_config():
    """显示 Bitget 配置信息"""
    print("\n📋 Bitget 配置信息:")
    print("=" * 50)
    
    # 现货配置
    spot_config = BitgetConfig.get_exchange_config()
    print("现货交易配置:")
    print(f"  交易所: {spot_config['name']}")
    print(f"  手续费: {spot_config['fee'] * 100}%")
    print(f"  API密钥状态: {'✅ 已配置' if spot_config['api_key'] else '❌ 未配置'}")
    
    # 合约配置
    futures_config = BitgetFuturesConfig.get_futures_config()
    print("\n合约交易配置:")
    print(f"  交易所: {futures_config['name']}")  
    print(f"  手续费: {futures_config['fee'] * 100}%")
    print(f"  杠杆倍数: {futures_config['futures_leverage']}x")
    print(f"  杠杆模式: {futures_config['futures_leverage_mode']}")
    
    # 支持的交易对
    pairs = BitgetConfig.get_trading_pairs()
    print(f"\n支持的交易对 ({len(pairs)} 个):")
    for i, pair in enumerate(pairs[:10], 1):
        print(f"  {i:2d}. {pair}")
    if len(pairs) > 10:
        print(f"     ... 还有 {len(pairs) - 10} 个")

if __name__ == "__main__":
    print("🎯 Bitget 交易所测试工具")
    print("=" * 50)
    
    # 显示配置
    show_bitget_config()
    
    # 测试连接
    if test_bitget_connection():
        # 测试合约
        test_bitget_futures()
    
    print("\n✨ 测试完成!")
    print("\n下一步:")
    print("1. 确保在 Secrets 中配置了 Bitget API 凭据")
    print("2. 运行: python test_bitget.py")
    print("3. 启动 Jesse: bash start-jesse.sh")
