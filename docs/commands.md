# 🛠️ 可用命令


## 使用 make.bat（Windows 快捷命令）（推荐）

```bash
make.bat help           # 显示所有可用命令
make.bat install        # 安装开发依赖
make.bat run            # 运行开发服务器
make.bat lint           # 代码质量检查
make.bat format         # 格式化代码
make.bat clean          # 清理临时文件
```

## 使用 uv 直接运行

```bash
# 安装依赖
uv sync --all-extras      # 安装所有依赖（包含开发工具）

# 运行服务器
uv run flask --app src run --debug              # 开发服务器

# 代码质量检查
uv run ruff check src                           # 代码检查（linting）
uv run ruff format --check src                  # 格式检查
uv run mypy src                                 # 类型检查

# 代码格式化
uv run ruff format src                          # 格式化代码
uv run ruff check --fix src                     # 自动修复 lint 问题

# Pre-commit 钩子（代码提交前自动检查）
uv run pre-commit install                       # 安装 git hooks（首次使用）
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


> 💡 **提示**：推荐直接使用 `uv` 命令以获得更好的灵活性，`make.bat` 提供常用命令的快捷方式。

## 常用工作流

### 开发流程

1. **启动开发服务器**
   ```bash
   make.bat run
   # 或
   uv run uvicorn src.app:app --reload
   ```

2. **代码修改后格式化**
   ```bash
   make.bat format
   # 或
   uv run ruff format src && uv run ruff check --fix src
   ```

3. **提交前检查**
   ```bash
   make.bat lint
   # 或
   uv run pre-commit run --all-files
   ```

### 添加新功能

1. **添加新依赖**
   ```bash
   uv add requests
   ```

2. **添加开发依赖**
   ```bash
   uv add --dev pytest
   ```

3. **同步依赖**
   ```bash
   uv sync
   ```
