# Flask WebAPI Scaffold

一个精简的、现代化的 Flask WebAPI 脚手架项目。

## ✨ 特性

- 🚀 **轻量级** - 只包含必需的依赖（Flask、pydantic）
- 📝 **简洁的 API** - 使用 Flask Blueprint 组织路由，支持版本化
- 🏗️ **应用工厂模式** - 灵活的应用创建和配置
- 🎨 **代码质量工具** - black、isort、flake8、mypy
- 📦 **现代化依赖管理** - 使用 pyproject.toml + **uv**
- 🔧 **Docker 支持** - 容器化部署配置
- 🎯 **可扩展架构** - 预留 models、services、middleware 目录

## 🚀 快速开始

### 1. 安装 uv 包管理器

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> 💡 更多 uv 使用方法请查看 [uv 使用指南](docs/uv-guide.md)

### 2. 克隆项目

```bash
git clone <your-repo>
cd PythonScaffolding
```

### 3. 安装依赖

```bash
# 使用快捷命令
make.bat install

# 或使用 uv 命令
uv sync --all-extras
```

### 4. 运行项目

```bash
# 使用快捷命令
make.bat run

# 或使用 uv 命令
uv run flask --app src run --debug
```

访问 http://localhost:5000

### 5. 首次提交前安装 Pre-commit（必须）

```bash
uv run pre-commit install
```

> 💡 Pre-commit 会在每次 `git commit` 前自动检查代码质量，详见 [Pre-commit 使用指南](docs/pre-commit.md)

## 📚 更多文档

- [📁 项目结构说明](docs/project-structure.md)
- [🛠️ 可用命令列表](docs/commands.md)
- [🔒 Pre-commit 使用指南](docs/pre-commit.md)
- [💡 uv 包管理器指南](docs/uv-guide.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT

---

**项目版本**: 1.0.0
**Python 版本**: >= 3.13
**包管理器**: uv
**最后更新**: 2026-01-28
