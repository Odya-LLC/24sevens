import multiprocessing


# bind = 'unix:apiagro.sock'
bind = '0.0.0.0:1221'
# umask = 0o007
timeout = 0
#logging
accesslog = 'logs/access.log'
errorlog = 'logs/err.log'
capture_output = True
log_level = "info"
loglevel = "info"
access_log_format = '%({X-Real-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" '