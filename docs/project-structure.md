# 📁 项目结构

```
PythonScaffolding/
├── src/                          # 源代码目录
│   ├── __init__.py              # Flask 应用工厂 (create_app)
│   │
│   ├── api/                     # API 路由层
│   │   └── v1/                  # API v1 版本
│   │       ├── __init__.py      # v1 blueprint
│   │       └── hello.py         # Hello 和 Ping 端点
│   │
│   ├── core/                    # 核心功能模块
│   │   ├── __init__.py
│   │   └── error_handlers.py    # HTTP 错误处理器
│   │
│   ├── models/                  # 数据模型（预留）
│   │   └── __init__.py
│   │
│   ├── services/                # 业务逻辑层（预留）
│   │   └── __init__.py
│   │
│   ├── middleware/              # 中间件（预留）
│   │   └── __init__.py
│   │
│   └── utils/                   # 工具函数（预留）
│       └── __init__.py
│
├── docs/                        # 项目文档
│   ├── project-structure.md    # 项目结构说明（本文档）
│   ├── commands.md             # 可用命令列表
│   ├── pre-commit.md           # Pre-commit 钩子说明
│   └── uv-guide.md             # uv 使用指南
│
├── .flake8                      # flake8代码风格配置
├── .gitignore                   # Git 忽略文件
├── .pre-commit-config.yaml      # Git pre-commit 钩子配置
├── Dockerfile                   # Docker 镜像构建
├── make.bat                     # 常用命令快捷方式（Windows）
├── pyproject.toml               # 项目配置和依赖
├── uv.toml                      # uv 镜像源配置（可选）
└── README.md                    # 项目文档
```

## 📝 目录说明

### `src/` - 源代码
应用的所有源代码都在此目录下。

- **`__init__.py`** - Flask 应用工厂模式，创建和配置应用实例 (create_app)

### `src/api/` - API 路由
基于 Blueprint 的 API 路由组织。

- **`v1/`** - API 第一版本
  - `__init__.py` - 创建 v1 blueprint
  - `hello.py` - Hello 和 Ping 端点实现

### `src/core/` - 核心功能
应用的核心功能模块。

- **`error_handlers.py`** - 统一的 HTTP 错误处理（404、500、400、403、405）

### `src/models/` - 数据模型（预留）
用于定义数据库模型（SQLAlchemy ORM 等）。

### `src/services/` - 业务逻辑层（预留）
用于实现复杂的业务逻辑，保持视图层简洁。

### `src/middleware/` - 中间件（预留）
用于实现请求/响应处理中间件（日志、认证等）。

### `src/utils/` - 工具函数（预留）
通用的辅助函数和工具。

## 🎯 设计原则

1. **简洁性** - 只保留必要的核心功能，避免过度设计
2. **可扩展性** - 预留目录结构，支持项目成长（models、services、middleware）
3. **标准化** - 遵循 Flask 和 Python 社区的最佳实践
4. **现代工具链** - 使用 uv 进行快速依赖管理
