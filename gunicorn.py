# Gunicorn 生产环境配置
# 使用方式: gunicorn -c gunicorn.py src.app:app

import multiprocessing
import os

# 服务器绑定
bind = f"{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', '8000')}"

# 工作进程数（推荐：CPU 核心数 * 2 + 1）
workers = int(os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1))

# 工作模式
worker_class = "sync"  # 可选: sync, gevent, eventlet, tornado

# 每个 worker 的线程数
threads = int(os.getenv("THREADS", 2))

# 超时设置（秒）
timeout = 120
keepalive = 5

# 日志配置
accesslog = "-"  # 输出到 stdout
errorlog = "-"  # 输出到 stderr
loglevel = os.getenv("LOG_LEVEL", "info")

# 进程命名
proc_name = "flask-api-scaffold"

# 优雅重启
graceful_timeout = 30
max_requests = 1000  # 每个 worker 处理多少请求后重启（防止内存泄漏）
max_requests_jitter = 50

# Preload app（提高启动速度，但会影响代码热重载）
preload_app = True
