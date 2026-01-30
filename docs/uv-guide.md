# 💡 uv 包管理器使用指南

## 📋 目录

- [为什么使用 uv？](#为什么使用-uv)
- [安装 uv](#安装-uv)
- [从零开始创建项目](#从零开始创建项目)
- [uv 常用命令](#uv-常用命令)
- [配置镜像源](#配置镜像源)
- [从 pip 迁移到 uv](#从-pip-迁移到-uv)
- [最佳实践](#最佳实践)
- [故障排查](#故障排查)

## 为什么使用 uv？

### uv vs pip

| 特性 | uv | pip |
|------|----|----|
| **速度** | ⚡ 快 10-100 倍 | 慢 |
| **锁文件** | ✅ `uv.lock` 确保一致性 | ❌ 需要额外工具 |
| **虚拟环境** | ✅ 内置自动管理 | 需要手动创建 |
| **依赖解析** | ✅ 智能冲突解决 | 基础 |
| **跨平台** | ✅ Rust 编写，性能一致 | Python 编写 |

## 安装 uv

### Windows
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

安装完成后，即可使用 `uv` 命令替代 `pip` 命令。

## 从零开始创建项目

### 📦 方法一：使用 uv init（推荐新项目）

```bash
# 创建新项目目录
mkdir my-flask-api
cd my-flask-api

# 初始化项目（创建 pyproject.toml）
uv init

# 指定 Python 版本
uv python pin 3.13

# 创建虚拟环境
uv venv

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 添加 Flask 依赖
uv add flask pydantic

# 添加开发依赖
uv add --dev ruff mypy pre-commit

# 添加生产依赖
uv add --optional cloud gunicorn
```

### 📝 方法二：手动创建 pyproject.toml（类似本项目）

**步骤 1**: 创建项目目录结构
```bash
mkdir my-flask-api
cd my-flask-api
```

**步骤 2**: 创建 `pyproject.toml` 文件
```toml
[project]
name = "my-flask-api"
version = "0.1.0"
description = "My Flask API project"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "Flask>=2.3.3",
    "pydantic>=2.3.0",
]

[project.optional-dependencies]
local = [
    "ruff>=0.8.0",
    "mypy>=1.5.1",
    "pre-commit>=4.5.1",
]
cloud = [
    "gunicorn>=21.2.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]

[tool.ruff]
line-length = 88
target-version = "py313"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP"]

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.13"
```

**步骤 3**: 创建 `.python-version` 文件
```bash
echo 3.13 > .python-version
```

**步骤 4**: 创建项目结构
```bash
# Windows PowerShell
New-Item -ItemType Directory -Path src, src\api, src\core, src\models, src\services, src\middleware, src\utils, docs
New-Item -ItemType File -Path src\__init__.py, src\app.py, README.md
```

**步骤 5**: 安装依赖
```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 同步所有依赖（包括开发依赖）
uv sync --all-extras
```

**步骤 6**: 初始化 Git 和 Pre-commit
```bash
# 初始化 Git
git init

# 创建 .gitignore
@"
__pycache__/
*.py[cod]
.venv/
*.egg-info/
.pytest_cache/
.mypy_cache/
.coverage
htmlcov/
dist/
build/
"@ | Out-File -FilePath .gitignore -Encoding utf8

# 安装 pre-commit hooks
uv run pre-commit install
```

### 🎯 项目模板结构

创建完成后，你的项目应该是这样的结构：

```
my-flask-api/
├── .venv/                 # 虚拟环境（uv venv 创建）
├── .python-version        # Python 版本标记
├── .gitignore             # Git 忽略文件
├── pyproject.toml         # 项目配置和依赖
├── uv.lock                # 依赖锁定文件（uv sync 生成）
├── README.md              # 项目说明
├── docs/                  # 文档目录
├── src/                   # 源代码目录
│   ├── __init__.py
│   ├── app.py             # Flask 应用入口
│   ├── api/               # API 路由
│   │   ├── __init__.py
│   │   └── user_controller.py
│   ├── core/              # 核心功能
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── models/            # 数据模型
│   │   ├── __init__.py
│   │   └── user_model.py
│   ├── services/          # 业务逻辑
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── middleware/        # 中间件
│   │   └── __init__.py
│   └── utils/             # 工具函数
│       └── __init__.py
└── tests/                 # 测试目录
```

### 🔧 创建开发脚本（可选）

创建 `make.bat`（Windows）或 `Makefile`（Linux/Mac）来简化常用命令：

```batch
@echo off

if "%1"=="" goto help
if "%1"=="install" goto install
if "%1"=="run" goto run
if "%1"=="lint" goto lint
goto help

:install
echo Installing dependencies...
uv sync --all-extras
goto end

:run
echo Starting FastAPI development server...
uv run uvicorn src.app:app --reload
goto end

:lint
echo Running code quality checks...
uv run ruff check src
uv run ruff format --check src
uv run mypy src
goto end

:help
echo Available commands:
echo   make.bat install  - Install dependencies
echo   make.bat run      - Run development server
echo   make.bat lint     - Run code quality checks
goto end

:end
```

## uv 常用命令

### 项目初始化

```bash
# 初始化新项目
uv init

# 初始化并创建虚拟环境
uv venv
```

### 依赖管理

```bash
# 同步依赖（根据 pyproject.toml）
uv sync

# 同步所有依赖（包括开发依赖）
uv sync --all-extras

# 添加生产依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name

# 移除依赖
uv remove package-name

# 查看依赖树
uv tree

# 更新所有依赖
uv lock --upgrade

# 更新特定依赖
uv lock --upgrade-package package-name
```

### 运行命令

```bash
# 运行 Python 脚本（自动使用虚拟环境）
uv run python script.py

# 运行 Flask 应用
uv run flask --app src run --debug

# 运行任何命令
uv run <command>
```

### 虚拟环境管理

```bash
# 创建虚拟环境
uv venv

# 创建指定 Python 版本的虚拟环境
uv venv --python 3.13

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 激活虚拟环境（macOS/Linux）
source .venv/bin/activate
```

### 其他实用命令

```bash
# 查看已安装的包
uv pip list

# 查看包信息
uv pip show package-name

# 冻结依赖（生成 requirements.txt）
uv pip freeze > requirements.txt

# 从 requirements.txt 安装
uv pip install -r requirements.txt
```

## 配置镜像源

### 方法 1: 创建 uv.toml 文件（推荐）

在项目根目录创建 `uv.toml` 文件：

```toml
# 清华大学镜像
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"

# 或使用阿里云镜像
# index-url = "https://mirrors.aliyun.com/pypi/simple"

# 或使用公司内部镜像
# index-url = "https://pypi.company.com/simple"
```

### 方法 2: 环境变量

```bash
# Windows PowerShell
$env:UV_INDEX_URL = "https://pypi.tuna.tsinghua.edu.cn/simple"

# macOS/Linux
export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
```

### 方法 3: 命令行参数

```bash
uv sync --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 常用国内镜像源

```toml
# 清华大学
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"

# 阿里云
index-url = "https://mirrors.aliyun.com/pypi/simple"

# 中国科技大学
index-url = "https://pypi.mirrors.ustc.edu.cn/simple"

# 豆瓣
index-url = "https://pypi.douban.com/simple"
```

## 从 pip 迁移到 uv

### requirements.txt 转换

```bash
# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 生成 uv.lock
uv lock

# 同步依赖到 pyproject.toml
# 手动编辑 pyproject.toml，然后运行
uv sync
```

### pipenv 迁移

```bash
# 导出 Pipfile.lock
pipenv requirements > requirements.txt

# 使用 uv 安装
uv pip install -r requirements.txt
```

## 最佳实践

1. **使用 `uv sync`** - 始终使用 `uv sync` 而不是 `uv pip install`，以确保依赖一致性
2. **提交 uv.lock** - 将 `uv.lock` 提交到 Git，确保团队依赖一致
3. **使用 extras** - 合理使用 extras 分组依赖（dev、test、prod）
4. **定期更新** - 定期运行 `uv lock --upgrade` 更新依赖
5. **使用镜像源** - 配置国内镜像源加速下载

## 故障排查

### 依赖冲突

```bash
# 查看冲突详情
uv sync --verbose

# 强制重新解析
uv lock --upgrade
```

### 清理缓存

```bash
# 清理 uv 缓存
uv cache clean

# 删除虚拟环境重新创建
rm -rf .venv
uv venv
uv sync
```

### 查看详细日志

```bash
# 显示详细日志
uv sync --verbose

# 显示调试信息
uv sync -vv
```

## 更多资源

- 官方文档: https://docs.astral.sh/uv/
- GitHub: https://github.com/astral-sh/uv
- Discord 社区: https://discord.gg/astral-sh
