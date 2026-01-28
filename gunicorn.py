# Gunicorn production configuration
# Usage: gunicorn -c gunicorn.py src.app:app

import multiprocessing
import os

# Server socket binding
bind = f"{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', '8000')}"

# Number of worker processes (recommended: CPU cores * 2 + 1)
workers = int(os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1))

# Worker class
worker_class = "sync"  # Options: sync, gevent, eventlet, tornado

# Number of threads per worker
threads = int(os.getenv("THREADS", 2))

# Timeout settings (seconds)
timeout = 120
keepalive = 5

# Logging configuration
accesslog = "-"  # Output to stdout
errorlog = "-"  # Output to stderr
loglevel = os.getenv("LOG_LEVEL", "info")

# Process naming
proc_name = "flask-api-scaffold"

# Graceful restart
graceful_timeout = 30
max_requests = 1000  # Restart worker after handling N requests (prevent memory leaks)
max_requests_jitter = 50

# Preload app (faster startup, but affects code hot reloading)
preload_app = True
