# FastAPI WebAPI Scaffold

一个精简的、现代化的 FastAPI WebAPI 脚手架项目。

## ✨ 特性

- 🚀 **轻量级** - 只包含必需的依赖（FastAPI、pydantic、uvicorn）
- 📝 **简洁的 API** - 使用 FastAPI APIRouter 组织路由，自动生成 OpenAPI 文档
- ⚡ **高性能** - 基于 Starlette 和 Pydantic，异步支持，性能优异
- 📖 **自动文档** - 自动生成交互式 API 文档（Swagger UI 和 ReDoc）
- 🏗️ **应用工厂模式** - 灵活的应用创建和配置
- 🎨 **代码质量工具** - ruff（超快的 linter + formatter）、mypy
- 📦 **现代化依赖管理** - 使用 pyproject.toml + **uv**（比 pip 快 10-100 倍）
- 🔒 **依赖锁定** - uv.lock 确保开发和生产环境依赖一致性
- 🔧 **Docker 支持** - 容器化部署配置
- 🎯 **可扩展架构** - 预留 models、services、middleware 目录
- ✅ **Pre-commit 钩子** - 自动代码质量检查
- 🌐 **生产就绪** - Gunicorn + Uvicorn 多进程部署支持

## 🚀 快速开始

### 方式一：使用本项目作为模板

#### 1. 安装 uv 包管理器

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> 💡 更多 uv 使用方法请查看 [uv 使用指南](docs/uv-guide.md)

#### 2. 克隆项目

```bash
git clone <your-repo>
cd PythonScaffolding
```

#### 3. 安装依赖

```bash
# 使用快捷命令
make.bat install

# 或使用 uv 命令
uv sync --all-extras
```

#### 4. 运行项目

```bash
# 开发模式（自动重载）
uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

# 或直接运行 app.py
uv run python -m src.app
```

访问：
- API 服务: http://localhost:8000
- 交互式文档 (Swagger UI): http://localhost:8000/docs
- 备用文档 (ReDoc): http://localhost:8000/redoc

**测试 API:**
```bash
# Get all users
curl http://localhost:8000/api/users

# Get user by ID
curl http://localhost:8000/api/users/1

# Get user by username
curl http://localhost:8000/api/users/username/johndoe

# 或者直接访问交互式文档进行测试
# http://localhost:8000/docs
```

#### 5. 首次提交前安装 Pre-commit（必须）

```bash
uv run pre-commit install
```

> 💡 Pre-commit 会在每次 `git commit` 前自动检查代码质量，详见 [Pre-commit 使用指南](docs/pre-commit.md)

---

### 方式二：从零开始创建新项目

如果你想基于本项目的架构创建自己的新项目，请参考：

📖 **[从零开始使用 uv 创建项目](docs/uv-guide.md#从零开始创建项目)**

该指南包含：
- ✅ 使用 `uv init` 初始化项目
- ✅ 配置 `pyproject.toml` 和依赖管理
- ✅ 创建项目目录结构
- ✅ 设置开发环境和工具链
- ✅ 配置 Git 和 Pre-commit



## 📚 更多文档

| 文档 | 说明 |
|------|------|
| [💡 uv 包管理器指南](docs/uv-guide.md) | **从零开始**创建项目、依赖管理、镜像配置、最佳实践 |
| [📁 项目结构说明](docs/project-structure.md) | 目录结构、各模块职责、设计理念 |
| [🛠️ 可用命令列表](docs/commands.md) | make.bat 命令、uv 命令速查表 |
| [🔒 Pre-commit 使用指南](docs/pre-commit.md) | Git hooks 配置、代码质量检查 |


## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT

---

**项目版本**: 1.0.0
**Python 版本**: >= 3.13
**包管理器**: uv (⚡ 比 pip 快 10-100 倍)
**代码质量**: ruff (⚡ 比 black + isort + flake8 快 10-100 倍)
**最后更新**: 2026-01-30
