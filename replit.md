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
│   └── __init__.py
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

## 最近更改

- 2025-10-09: 初始化 Jesse 项目，配置 PostgreSQL (Neon) 和 Redis
- 2025-10-09: 成功部署 Jesse 1.10.10 框架
- 2025-10-09: 配置 Web 仪表板运行在 port 5000

## 环境变量

项目使用 .env 文件配置以下变量：
- PASSWORD: 仪表板密码
- APP_PORT: Web 服务端口（5000）
- POSTGRES_HOST, POSTGRES_PORT, POSTGRES_NAME, POSTGRES_USERNAME, POSTGRES_PASSWORD
- REDIS_HOST, REDIS_PORT
- LICENSE_API_TOKEN: (实时交易插件使用)
