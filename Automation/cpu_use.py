import psutil

usage = psutil.cpu_percent(interval=0.1)
print("CPU Usage: %d%%" % usage)