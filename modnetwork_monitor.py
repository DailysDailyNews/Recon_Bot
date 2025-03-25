import psutil

def monitor_network():
  connections = psutil.net_connections()
    for conn in connections:
      print(f"PID: {conn.pid}, IP: {conn.laddr.ip}, PORT: {conn.laddr.port}")
