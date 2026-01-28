# 📁 项目结构

```
PythonScaffolding/
├── src/                          # 源代码目录
│   ├── __init__.py              # Flask 应用工厂 (create_app)
│   ├── app.py                   # WSGI 入口点 (用于 Gunicorn)
│   │
│   ├── api/                     # API 路由层 (Controller)
│   │   ├── __init__.py          # API 模块导出
│   │   └── user_controller.py   # 用户 API 端点 (CRUD)
│   │
│   ├── core/                    # 核心功能模块
│   │   ├── __init__.py
│   │   ├── config.py            # 配置管理 (Local/Cloud)
│   │   ├── database.py          # Peewee ORM 配置和连接管理
│   │   ├── decorators.py        # 自定义装饰器（预留）
│   │   ├── error_handlers.py    # 全局 HTTP 错误处理器
│   │   ├── exceptions.py        # 自定义异常类
│   │   ├── logging.py           # 日志系统配置
│   │   └── response.py          # 标准化 API 响应格式
│   │
│   ├── models/                  # 数据模型 (Peewee ORM)
│   │   ├── __init__.py
│   │   └── user_model.py        # 用户模型
│   │
│   ├── services/                # 业务逻辑层
│   │   ├── __init__.py
│   │   └── user_service.py      # 用户业务逻辑（CRUD 操作）
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
├── .env                         # 环境变量配置 (需手动创建)
├── .flake8                      # flake8 代码风格配置
├── .gitignore                   # Git 忽略文件
├── .pre-commit-config.yaml      # Git pre-commit 钩子配置
├── Dockerfile                   # Docker 镜像构建
├── gunicorn.py                  # Gunicorn 生产环境配置
├── make.bat                     # 常用命令快捷方式（Windows）
├── pyproject.toml               # 项目配置和依赖
├── uv.toml                      # uv 镜像源配置（可选）
├── uv.lock                      # 依赖锁定文件
└── README.md                    # 项目文档
```

## 📝 目录说明

### `src/` - 源代码
应用的所有源代码都在此目录下。

- **`__init__.py`** - Flask 应用工厂模式，创建和配置应用实例 (create_app)
  - 初始化数据库连接
  - 注册 Blueprint
  - 配置全局错误处理器
  - 设置日志系统

- **`app.py`** - WSGI 入口点
  - 用于 Gunicorn 等 WSGI 服务器
  - 开发模式也可直接运行

### `src/api/` - API 路由 (Controller 层)
基于 Blueprint 的 API 路由组织。

- **`user_controller.py`** - 用户 API 端点
  - `GET /api/users` - 获取所有用户
  - `GET /api/users/<id>` - 根据 ID 获取用户
  - `POST /api/users` - 创建新用户
  - `PUT /api/users/<id>` - 更新用户信息
  - `DELETE /api/users/<id>` - 删除用户

### `src/core/` - 核心功能
应用的核心功能模块。

- **`config.py`** - 配置管理
  - 支持 Local/Cloud 环境切换
  - 基于环境变量加载配置
  - 使用 `python-dotenv` 支持 .env 文件

- **`database.py`** - Peewee ORM 配置
  - 支持 MySQL/PostgreSQL/SQLite
  - 自动连接池管理
  - Flask 请求钩子集成
  - BaseModel 基类
  - `@atomic()` 事务装饰器

- **`response.py`** - 标准化 API 响应
  - `success_response()` - 成功响应
  - `error_response()` - 错误响应
  - `created_response()` - 201 创建成功
  - `paginated_response()` - 分页响应
  - `no_content_response()` - 204 无内容

- **`exceptions.py`** - 自定义异常类
  - `ValidationError` - 参数验证错误 (400)
  - `AuthenticationError` - 认证失败 (401)
  - `AuthorizationError` - 权限不足 (403)
  - `NotFoundError` - 资源不存在 (404)
  - `ConflictError` - 资源冲突 (409)
  - `ServiceUnavailableError` - 服务不可用 (503)

- **`error_handlers.py`** - 全局错误处理
  - 统一的 HTTP 错误处理（404、500、400、403、405）
  - 自定义异常处理
  - Werkzeug 异常处理

- **`logging.py`** - 日志系统
  - 请求上下文感知的日志格式
  - 支持标准格式和 JSON 格式
  - 可配置日志级别

### `src/models/` - 数据模型 (Model 层)
使用 Peewee ORM 定义数据模型。

- **`user_model.py`** - 用户数据模型
  - 继承自 `BaseModel`
  - 定义字段和类型
  - 提供 `to_dict()` 序列化方法

### `src/services/` - 业务逻辑层 (Service 层)
实现业务逻辑，保持视图层简洁。

- **`user_service.py`** - 用户业务逻辑
  - `get_all_users()` - 获取所有用户
  - `get_user_by_id()` - 根据 ID 获取用户
  - `create_user()` - 创建用户（带事务）
  - `update_user()` - 更新用户（带事务）
  - `delete_user()` - 删除用户（带事务）

### `src/middleware/` - 中间件（预留）
用于实现请求/响应处理中间件（日志、认证等）。

### `src/utils/` - 工具函数（预留）
通用的辅助函数和工具。

## 🎯 设计原则

1. **分层架构** - Controller → Service → Model 清晰分离
   - Controller 负责请求响应
   - Service 负责业务逻辑
   - Model 负责数据持久化

2. **应用工厂模式** - 灵活的应用创建和配置
   - 支持多环境配置
   - 易于测试和扩展

3. **依赖注入** - 通过函数参数传递依赖
   - 提高代码可测试性
   - 降低耦合度

4. **统一响应格式** - 标准化的 JSON 响应
   - 成功/错误响应格式一致
   - 便于前端处理

5. **异常处理** - 自定义异常体系
   - 语义化的异常类
   - 全局错误处理器

6. **现代工具链** - 使用 uv 进行快速依赖管理
   - 比 pip 快 10-100 倍
   - 与 pyproject.toml 完美集成

## 🔄 请求流程

```
客户端请求
    ↓
Flask 路由
    ↓
Controller (api/)
    ↓
Service (services/)
    ↓
Model (models/)
    ↓
Database
    ↓
返回结果
    ↓
标准化响应 (response.py)
    ↓
客户端接收
```

## 🔌 扩展建议

### 添加新功能模块

1. 在 `models/` 创建数据模型
2. 在 `services/` 创建业务逻辑
3. 在 `api/` 创建 Controller
4. 在 `src/__init__.py` 注册 Blueprint

### 添加中间件

在 `middleware/` 目录创建中间件，例如：
- 认证中间件
- 请求日志中间件
- CORS 中间件
- 限流中间件

### 添加工具函数

在 `utils/` 目录添加通用工具，例如：
- 日期时间处理
- 加密解密
- 文件上传
- 邮件发送
