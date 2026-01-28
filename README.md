# Flask WebAPI Scaffold

一个精简的、现代化的 Flask WebAPI 脚手架项目，基于应用工厂模式和分层架构设计。

## ✨ 特性

- 🚀 **轻量级** - 核心依赖（Flask、Peewee ORM、Pydantic、python-dotenv）
- 📝 **RESTful API** - 使用 Flask Blueprint 组织路由，标准化响应格式
- 🗄️ **ORM 集成** - Peewee ORM，支持 MySQL/PostgreSQL/SQLite
- 🏗️ **应用工厂模式** - 灵活的应用创建和配置管理
- 🎯 **分层架构** - Controller → Service → Model 清晰分离
- ⚡ **事务管理** - 装饰器式事务处理（@atomic）
- 📊 **统一响应格式** - 标准化的成功/错误响应
- 🔍 **异常处理** - 自定义异常体系和全局错误处理器
- 📝 **日志系统** - 请求上下文感知的日志记录
- 🎨 **代码质量工具** - black、isort、flake8、mypy、pre-commit
- 📦 **现代化依赖管理** - 使用 pyproject.toml + **uv** 超快速包管理
- 🔧 **Docker 支持** - 生产级 Dockerfile + Gunicorn 配置
- 🌍 **环境配置** - 支持 local/cloud 环境，基于 .env 配置

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

**测试 API:**
```bash
# Health check
curl http://localhost:5000/health

# Database health check
curl http://localhost:5000/health/db

# Get all users
curl http://localhost:5000/api/users

# Get user by ID
curl http://localhost:5000/api/users/1

# Create a new user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30}'

# Update user
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "age": 25}'

# Delete user
curl -X DELETE http://localhost:5000/api/users/1
```

### 5. 首次提交前安装 Pre-commit（必须）

```bash
uv run pre-commit install
```

> 💡 Pre-commit 会在每次 `git commit` 前自动检查代码质量，详见 [Pre-commit 使用指南](docs/pre-commit.md)

## 📦 项目结构

```
PythonScaffolding/
├── src/                          # 源代码目录
│   ├── __init__.py              # 应用工厂 (create_app)
│   ├── app.py                   # WSGI 入口点
│   │
│   ├── api/                     # API 控制器层 (Controller)
│   │   └── user_controller.py   # 用户 CRUD API
│   │
│   ├── core/                    # 核心功能模块
│   │   ├── config.py            # 配置管理（Local/Cloud）
│   │   ├── database.py          # 数据库连接和 ORM 基类
│   │   ├── decorators.py        # 自定义装饰器
│   │   ├── error_handlers.py    # 全局异常处理
│   │   ├── exceptions.py        # 自定义异常类
│   │   ├── logging.py           # 日志配置
│   │   └── response.py          # 统一响应格式
│   │
│   ├── models/                  # 数据模型层 (Model)
│   │   └── user_model.py        # 用户 Peewee ORM 模型
│   │
│   ├── services/                # 业务逻辑层 (Service)
│   │   └── user_service.py      # 用户业务逻辑
│   │
│   ├── middleware/              # 中间件（可扩展）
│   └── utils/                   # 工具函数（可扩展）
│
├── docs/                        # 项目文档
│   ├── commands.md              # 可用命令列表
│   ├── pre-commit.md            # Pre-commit 指南
│   ├── project-structure.md     # 详细结构说明
│   └── uv-guide.md              # uv 使用指南
│
├── Dockerfile                   # Docker 镜像构建
├── gunicorn.py                  # Gunicorn 生产配置
├── make.bat                     # Windows 快捷命令
├── pyproject.toml               # 项目配置和依赖
└── uv.lock                      # 依赖锁定文件
```

### 核心模块说明

#### 🎯 分层架构
- **Controller** (`api/`) - 处理 HTTP 请求和响应
- **Service** (`services/`) - 业务逻辑处理
- **Model** (`models/`) - 数据模型和数据库交互

#### 🔧 核心功能
- **database.py** - Peewee ORM 配置，支持 MySQL/PostgreSQL/SQLite，自动连接池管理
- **response.py** - 统一 JSON 响应格式（成功/错误/分页）
- **exceptions.py** - 自定义异常（ValidationError, NotFoundError, 等）
- **config.py** - 环境配置管理（通过 FLASK_ENV 切换）

## 🔌 数据库配置

项目使用 **Peewee ORM**，支持多种数据库：

```bash
# .env 文件配置示例

# MySQL
DATABASE_URL=mysql://user:password@localhost:3306/dbname

# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# SQLite
DATABASE_URL=sqlite:///./data.db

# 其他配置
FLASK_ENV=local          # local 或 cloud
LOG_LEVEL=DEBUG          # DEBUG, INFO, WARNING, ERROR
```

## 🚀 API 端点

### 基础端点
- `GET /` - API 信息
- `GET /health` - 健康检查
- `GET /health/db` - 数据库健康检查

### 用户管理
- `GET /api/users` - 获取所有用户
- `GET /api/users/<id>` - 获取单个用户
- `POST /api/users` - 创建用户
- `PUT /api/users/<id>` - 更新用户
- `DELETE /api/users/<id>` - 删除用户

### 响应格式

**成功响应：**
```json
{
  "success": true,
  "message": "User retrieved successfully",
  "data": {
    "id": 1,
    "name": "John Doe",
    "age": 30
  }
}
```

**错误响应：**
```json
{
  "success": false,
  "message": "User with ID 999 not found"
}
```

## 🐳 Docker 部署

```bash
# 构建镜像
docker build -t flask-api-scaffold .

# 运行容器
docker run -p 8000:8000 \
  -e FLASK_ENV=cloud \
  -e DATABASE_URL=mysql://user:pass@host:3306/db \
  flask-api-scaffold
```

## 🛠️ 开发工具

### 代码质量工具

```bash
# 代码格式化
make.bat format

# 代码检查
make.bat lint

# 类型检查
make.bat type-check

# 运行所有检查
make.bat check
```

## 🔌 扩展指南

### 添加新的 API 模块

1. **创建 Model** (`src/models/`)
```python
from peewee import CharField
from src.core.database import BaseModel

class ProductModel(BaseModel):
    name = CharField(max_length=100)

    class Meta:
        table_name = "product"
```

2. **创建 Service** (`src/services/`)
```python
from src.core.database import atomic
from src.models.product_model import ProductModel

@atomic()
def create_product(name: str):
    return ProductModel.create(name=name)
```

3. **创建 Controller** (`src/api/`)
```python
from flask import Blueprint
from src.core.response import success_response
from src.services import product_service

ProductController = Blueprint("product", __name__, url_prefix="/api/products")

@ProductController.route("", methods=["GET"])
def get_products():
    products = product_service.get_all_products()
    return success_response(data=products)
```

4. **注册 Blueprint** (`src/__init__.py`)
```python
from src.api.product_controller import ProductController
app.register_blueprint(ProductController)
```

## 📚 技术栈

### 核心框架
- **Flask 2.3+** - 轻量级 Web 框架
- **Peewee 3.17+** - 简洁的 ORM
- **Pydantic 2.3+** - 数据验证
- **PyMySQL 1.1+** - MySQL 数据库驱动

### 开发工具
- **uv** - 超快速 Python 包管理器
- **black** - 代码格式化
- **isort** - import 排序
- **flake8** - 代码风格检查
- **mypy** - 静态类型检查
- **pre-commit** - Git 提交钩子

### 生产部署
- **Gunicorn** - WSGI HTTP 服务器
- **Docker** - 容器化部署

## 📚 更多文档

## 📚 更多文档

- [📁 项目结构说明](docs/project-structure.md)
- [🛠️ 可用命令列表](docs/commands.md)
- [🔒 Pre-commit 使用指南](docs/pre-commit.md)
- [💡 uv 包管理器指南](docs/uv-guide.md)

## 💡 最佳实践

1. **使用环境变量** - 敏感信息通过 `.env` 文件配置
2. **事务管理** - 写操作使用 `@atomic()` 装饰器
3. **异常处理** - 使用自定义异常类（ValidationError, NotFoundError 等）
4. **日志记录** - 在关键操作点添加日志
5. **代码质量** - 提交前运行 `make.bat check`
6. **分层原则** - Controller 只处理请求响应，业务逻辑放在 Service 层
7. **统一响应** - 使用 `success_response()` 和 `error_response()` 标准化 API 响应

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

提交前请确保：
- ✅ 通过所有代码质量检查
- ✅ 添加必要的测试
- ✅ 更新相关文档

## 📄 License

MIT

---

**项目版本**: 1.0.0
**Python 版本**: >= 3.13
**包管理器**: uv
**最后更新**: 2026-01-28
