# Jesse Trading Framework

完整的加密货币算法交易框架，基于 Jesse 官方项目模板。

## 项目概述

这是一个一模一样的 Jesse 交易框架，包含：
- 回测引擎（支持零前视偏差、滑点、手续费模拟）
- 策略开发框架
- 300+ 技术指标
- Web 仪表板（运行在 port 5000）
- PostgreSQL 数据库（Replit Neon）
- Redis 缓存系统

## 当前配置

### 框架版本
- Jesse: 1.10.10
- Python: 3.11
- PostgreSQL: 17 (Neon)
- Redis: 7.2.10

### 数据库
- PostgreSQL: 使用 Replit 提供的 Neon 数据库
- Redis: 本地运行在 port 6379

### 服务状态
- Web 仪表板: http://localhost:5000
- 启动命令: `bash start-jesse.sh`
- Workflow: "Jesse Trading Framework" 已配置并运行

## 项目结构

```
├── .env                    # 环境配置（包含数据库凭据）
├── .env.example           # 环境配置模板
├── start-jesse.sh         # 启动脚本
├── strategies/            # 交易策略目录
│   ├── ExampleStrategy/   # 示例策略
│   ├── QuantumStrategy/   # 量子增强策略（前十大币种）
│   └── __init__.py
├── config/                # 配置文件
│   └── trading_pairs.py   # 交易对配置
├── storage/               # 存储目录
│   ├── logs/             # 日志文件
│   └── __init__.py
└── docker/               # Docker 配置
    └── docker-compose.yml
```

## 使用方法

### 启动框架
```bash
bash start-jesse.sh
```

### Jesse 命令
```bash
jesse run          # 启动 Web 仪表板
jesse --help       # 查看所有命令
```

## Jesse 生态系统工具

### 数据导入工具
- **candle-importer-script**: 自动从交易所获取历史K线数据，持续更新数据库用于回测

### 其他工具
- **jesse-trades-info**: 解析回测 JSON 文件，以表格和图表展示交易结果
- **jesse-bulk**: 批量测试工具
- **jesse-optuna**: 使用 Optuna 进行策略优化
- **jesse-strategy-merger**: 合并多个策略

## 交易策略

### QuantumStrategy（量子增强策略）
- **支持币种**：前十大加密货币（BTC, ETH, BNB, SOL, XRP, ADA, DOGE, AVAX, DOT, MATIC）
- **支持交易所**：Bitget, OKX
- **策略类型**：双均线 + RSI 组合策略
- **风险管理**：每笔交易 1% 风险，2% 止损，5% 止盈
- **特性**：移动止损、动态仓位管理

## 实盘交易配置

### 必需的 API 密钥（在 Secrets 中配置）：
- `LICENSE_API_TOKEN` - Jesse 实盘许可证
- `BITGET_API_KEY` - Bitget API Key
- `BITGET_API_SECRET` - Bitget API Secret  
- `BITGET_PASSPHRASE` - Bitget Passphrase
- `OKX_API_KEY` - OKX API Key
- `OKX_API_SECRET` - OKX API Secret
- `OKX_PASSPHRASE` - OKX Passphrase

## 最近更改

- 2025-10-09: 初始化 Jesse 项目，配置 PostgreSQL (Neon) 和 Redis
- 2025-10-09: 成功部署 Jesse 1.10.10 框架
- 2025-10-09: 配置 Web 仪表板运行在 port 5000
- 2025-10-09: 添加 QuantumStrategy 量子增强策略
- 2025-10-09: 配置前十大加密货币交易对
- 2025-10-09: 集成 Bitget 和 OKX 交易所支持
- 2025-10-09: 项目已推送至 GitHub (Vicliu1213/JesseTrading)

## 环境变量

项目使用 .env 文件配置以下变量：
- PASSWORD: 仪表板密码
- APP_PORT: Web 服务端口（5000）
- POSTGRES_HOST, POSTGRES_PORT, POSTGRES_NAME, POSTGRES_USERNAME, POSTGRES_PASSWORD
- REDIS_HOST, REDIS_PORT
- LICENSE_API_TOKEN: (实时交易插件使用)
