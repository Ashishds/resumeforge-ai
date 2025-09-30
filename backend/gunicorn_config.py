"""
Gunicorn Configuration for Production Deployment
Optimized for fast response times and efficient resource usage
"""

import multiprocessing
import os

# Server socket
bind = f"0.0.0.0:{os.getenv('PORT', 8000)}"
backlog = 2048

# Worker processes
workers = int(os.getenv('WEB_CONCURRENCY', 1))  # 1 worker for free tier
worker_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 1000
max_requests = 1000  # Restart workers after 1000 requests (prevent memory leaks)
max_requests_jitter = 50
timeout = 120  # 120 seconds timeout for AI processing
keepalive = 5  # 5 seconds keepalive

# Logging
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
loglevel = os.getenv('LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'resumeforge-api'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Performance
preload_app = True  # Load application code before workers are forked
reuse_port = True if os.name != 'nt' else False  # Enable SO_REUSEPORT

def post_fork(server, worker):
    """Called just after a worker has been forked"""
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    """Called just before a worker is forked"""
    pass

def pre_exec(server):
    """Called just before a new master process is forked"""
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    """Called just after the server is started"""
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    """Called when a worker receives the SIGINT or SIGQUIT signal"""
    worker.log.info("worker received INT or QUIT signal")

def worker_abort(worker):
    """Called when a worker receives the SIGABRT signal"""
    worker.log.info("worker received SIGABRT signal")
