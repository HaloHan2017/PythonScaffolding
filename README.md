# Flask WebAPI Scaffold

一个精简的、现代化的 Flask WebAPI 脚手架项目。

## ✨ 特性

- 🚀 **轻量级** - 只包含必需的依赖（Flask、pydantic）
- 📝 **简洁的 API** - 使用 Flask Blueprint 组织路由，支持版本化
- 🏗️ **应用工厂模式** - 灵活的应用创建和配置
- 🎨 **代码质量工具** - black、isort、flake8、mypy
- 📦 **现代化依赖管理** - 使用 pyproject.toml + **uv**
- 🔧 **生产就绪** - 集成 gunicorn/waitress 配置
- 🎯 **可扩展架构** - 预留 models、services、middleware 目录

## 📋 依赖

### 核心依赖
- **Flask** `>=2.3.3` - Web 框架
- **pydantic** `>=2.3.0` - 数据验证

### 开发依赖
- **black** `>=23.9.1` - 代码格式化
- **isort** `>=5.12.0` - import 排序
- **flake8** `>=6.1.0` - 代码检查
- **mypy** `>=1.5.1` - 类型检查
- **pre-commit** `>=4.5.1` - Git 提交前钩子

### 生产依赖 (Cloud)
- **gunicorn** `>=21.2.0` - 生产环境 WSGI 服务器（Linux/macOS）
- **waitress** `>=2.1.2` - 生产环境 WSGI 服务器（Windows）

## 🚀 快速开始

### 前置要求

- **Python 3.13+**
- **uv** - 现代化的 Python 包管理器

#### 安装 uv
```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 1. 克隆项目
```bash
git clone <your-repo>
cd PythonScaffolding
```

### 2. 安装依赖

uv 会自动创建虚拟环境并安装依赖。

#### 💻 Local 环境（本地开发）

**Windows:**
```bash
uv sync --all-extras
```

#### ☁️ Cloud 环境（线上生产）

**Windows:**
```bash
uv sync --extra prod
```

### 3. 运行应用

#### 💻 Local 环境（本地开发）

**Windows:**
```bash
uv run flask --app src run --debug
```

访问 http://localhost:5000

#### ☁️ Cloud 环境（线上部署）

**Linux:**
```bash
uv run gunicorn -c gunicorn.py src.app:app
```

**Windows:**
```bash
uv run python waitress_serve.py
```

## 📁 项目结构

```
PythonScaffolding/
├── src/                          # 源代码目录
│   ├── __init__.py              # Flask 应用工厂
│   ├── app.py                   # WSGI 入口点
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
├── .gitignore                  # Git 忽略文件
├── .pre-commit-config.yaml     # Git pre-commit 钩子
├── Dockerfile                  # Docker 镜像构建
├── gunicorn.py                 # Gunicorn 生产配置（Linux/macOS）
├── waitress_serve.py           # Waitress 生产配置（Windows）
├── Makefile                    # 常用命令快捷方式
├── pyproject.toml             # 项目配置和依赖
└── README.md                   # 项目文档
```

### 📝 目录说明

#### `src/` - 源代码
应用的所有源代码都在此目录下。

- **`__init__.py`** - Flask 应用工厂模式，创建和配置应用实例
- **`app.py`** - WSGI 入口点，供 gunicorn 等生产服务器使用

#### `src/api/` - API 路由
基于 Blueprint 的 API 路由组织。

- **`v1/`** - API 第一版本
  - `__init__.py` - 创建 v1 blueprint
  - `hello.py` - Hello 和 Ping 端点实现

#### `src/core/` - 核心功能
应用的核心功能模块。

- **`error_handlers.py`** - 统一的 HTTP 错误处理（404、500、400、403、405）

#### `src/models/` - 数据模型（预留）
用于定义数据库模型（SQLAlchemy ORM 等）。

#### `src/services/` - 业务逻辑层（预留）
用于实现复杂的业务逻辑，保持视图层简洁。

#### `src/middleware/` - 中间件（预留）
用于实现请求/响应处理中间件（日志、认证等）。

#### `src/utils/` - 工具函数（预留）
通用的辅助函数和工具。


## 🎯 设计原则

1. **简洁性** - 只保留必要的核心功能，避免过度设计
2. **可扩展性** - 预留目录结构，支持项目成长（models、services、middleware）
3. **标准化** - 遵循 Flask 和 Python 社区的最佳实践
4. **环境隔离** - Local 和 Cloud 环境配置分离
5. **现代工具链** - 使用 uv 进行快速依赖管理

## 🔒 Pre-commit 钩子

Pre-commit 会在你每次 `git commit` 之前自动运行代码检查，确保代码质量。

### 首次设置

```bash
# 安装 pre-commit hooks 到 git
uv run pre-commit install
```

### 使用方式

安装后，pre-commit 会在每次 `git commit` 时自动运行。如果检查失败，提交会被阻止，你需要修复问题后重新提交。

**手动运行 pre-commit：**

```bash
# 检查所有文件
uv run pre-commit run --all-files

# 只检查暂存的文件（即将提交的文件）
uv run pre-commit run

# 检查特定文件
uv run pre-commit run --files src/app.py

# 更新 pre-commit 钩子到最新版本
uv run pre-commit autoupdate
```

### Pre-commit 检查项

项目配置了以下检查（`.pre-commit-config.yaml`）：

1. **trailing-whitespace** - 移除行尾空格
2. **end-of-file-fixer** - 确保文件以换行符结尾
3. **check-yaml** - 验证 YAML 文件格式
4. **check-added-large-files** - 防止提交大文件
5. **check-merge-conflict** - 检查合并冲突标记
6. **check-case-conflict** - 检查文件名大小写冲突
7. **detect-private-key** - 检测私钥泄露
8. **black** - 代码格式化
9. **isort** - import 语句排序
10. **flake8** - 代码风格检查
11. **mypy** - 类型检查

### 跳过 Pre-commit（不推荐）

如果确实需要跳过检查（不推荐），可以使用：

```bash
git commit --no-verify -m "commit message"
```

## 🛠️ 可用命令

### 使用 uv 直接运行（推荐）

```bash
# 安装依赖
uv sync --all-extras      # Local 环境（包含所有开发工具）
uv sync --extra prod      # Cloud 环境（仅生产依赖）

# 运行服务器
uv run flask --app src run --debug              # Local 服务器
uv run gunicorn -c gunicorn.py src.app:app      # Cloud 服务器（仅 Linux/macOS）
uv run python waitress_serve.py                 # Cloud 服务器（Windows）

# 代码质量
uv run flake8 src                               # 代码检查
uv run mypy src                                 # 类型检查
uv run black --check src                        # 格式检查
uv run isort --check-only src                   # import 排序检查

# 代码格式化
uv run black src                                # 格式化代码
uv run isort src                                # 排序 imports

# Pre-commit 钩子（代码提交前自动检查）
uv run pre-commit install                       # 安装 git hooks（首次使���）
uv run pre-commit run --all-files               # 手动运行所有检查
uv run pre-commit run                           # 只检查暂存的文件
uv run pre-commit autoupdate                    # 更新 pre-commit 钩子版本

# 依赖管理
uv add package-name                             # 添加新依赖
uv add --dev package-name                       # 添加开发依赖
uv remove package-name                          # 移除依赖
uv sync                                         # 同步依赖
uv tree                                         # 查看依赖树
uv lock --upgrade                               # 更新所有依赖
```

### 使用 Makefile（仅 macOS/Linux）

```bash
make help         # 显示所有可用命令
make install      # 安装开发依赖（Local 环境）
make install-prod # 安装生产依赖（Cloud 环境）
make run          # 运行 Local 服务器
make run-prod     # 运行 Cloud 服务器
make lint         # 代码质量检查
make format       # 格式化代码
make clean        # 清理临时文件
```

> 💡 **提示**：Windows 用户请直接使用 `uv` 命令，macOS/Linux 用户可以使用 `make` 或 `uv` 命令。

## 💡 为什么使用 uv？

### uv vs pip

| 特性 | uv | pip |
|------|----|----|
| **速度** | ⚡ 快 10-100 倍 | 慢 |
| **锁文件** | ✅ `uv.lock` 确保一致性 | ❌ 需要额外工具 |
| **虚拟环境** | ✅ 内置自动管理 | 需要手动创建 |
| **依赖解析** | ✅ 智能冲突解决 | 基础 |
| **跨平台** | ✅ Rust 编写，性能一致 | Python 编写 |

### uv 常用命令

```bash
# 初始化项目（已完成）
uv init

# 同步依赖（根据 pyproject.toml）
uv sync

# 添加依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name

# 移除依赖
uv remove package-name

# 运行命令（自动使用虚拟环境）
uv run python script.py
uv run flask run

# 查看依赖树
uv tree

# 更新所有依赖
uv lock --upgrade
```

### 配置镜像源

**公司内部 PyPI 镜像：**

创建 `uv.toml` 文件：
```toml
[tool.uv]
index-url = "https://pypi.company.com/simple"
```

**常用国内镜像：**

```toml
# 清华大学镜像（推荐）
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

```toml
# 阿里云镜像
[tool.uv]
index-url = "https://mirrors.aliyun.com/pypi/simple"
```

```toml
# 腾讯云镜像
[tool.uv]
index-url = "https://mirrors.cloud.tencent.com/pypi/simple"
```

```toml
# 华为云镜像
[tool.uv]
index-url = "https://repo.huaweicloud.com/repository/pypi/simple"
```

**使用自签名证书的私有源：**

```toml
[tool.uv]
index-url = "https://pypi.company.com/simple"
trusted-hosts = ["pypi.company.com"]
```

**多个镜像源（主源+备用）：**

```toml
[tool.uv]
index-url = "https://pypi.company.com/simple"
extra-index-url = [
    "https://pypi.org/simple",  # 官方源作为备用
]
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT

---

**项目版本**: 1.0.0
**Python 版本**: >= 3.13
**包管理器**: uv
**最后更新**: 2025-01-27
