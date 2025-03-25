import socket

def watch_ports():
  target_ip = "0.0.0.0"
  target_port = 80
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((target_ip, target_port))
    s.listen(5)
    print(f"Listening on {target_port}")
