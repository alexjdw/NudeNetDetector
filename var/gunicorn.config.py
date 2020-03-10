import os

bind = "0.0.0.0:80"
workers = int(os.environ.get("WORKERS") or 1)
keepalive = 120
timeout = keepalive
loglevel = "info"
access_log = "-"
