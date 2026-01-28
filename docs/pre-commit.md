# 🔒 Pre-commit 钩子使用指南

Pre-commit 会在你每次 `git commit` 之前自动运行代码检查，确保代码质量。

## 首次设置

```bash
# 安装 pre-commit hooks 到 git
uv run pre-commit install
```

## 使用方式

安装后，pre-commit 会在每次 `git commit` 时自动运行。如果检查失败，提交会被阻止，你需要修复问题后重新提交。

### 手动运行 pre-commit

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

## Pre-commit 检查项

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

## 工作流程示例

### 正常提交流程

```bash
# 1. 暂存文件
git add .

# 2. 提交（pre-commit 自动运行）
git commit -m "feat: add new feature"

# 如果检查通过，提交成功
# 如果检查失败，会显示错误信息
```

### 修复检查失败

如果 pre-commit 检查失败：

```bash
# 1. 查看错误信息，pre-commit 会告诉你哪些文件有问题

# 2. 修复问题（很多问题会自动修复）
# black 和 isort 会自动格式化代码
# 其他问题需要手动修复

# 3. 重新暂存修复后的文件
git add .

# 4. 再次提交
git commit -m "feat: add new feature"
```

## 跳过 Pre-commit（不推荐）

如果确实需要跳过检查（不推荐），可以使用：

```bash
git commit --no-verify -m "commit message"
```

> ⚠️ **警告**：跳过检查可能导致代码质量下降，仅在紧急情况下使用。

## 常见问题

### Q: Pre-commit 运行很慢怎么办？

A: Pre-commit 首次运行会下载和安装钩子环境，后续运行会很快。如果持续很慢，可以尝试：
```bash
# 清理并重新安装
uv run pre-commit clean
uv run pre-commit install
```

### Q: 如何临时禁用某个检查？

A: 编辑 `.pre-commit-config.yaml` 文件，在对应的钩子前添加 `#` 注释，或设置 `exclude` 排除特定文件。

### Q: 如何只运行特定的检查？

A: 使用 `--hook-stage` 参数：
```bash
uv run pre-commit run black --all-files
uv run pre-commit run flake8 --all-files
```
