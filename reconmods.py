import socket

def recon_scan():
  target = "example.com"
  for port in range(20, 1025):
    s =
socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
      print(f"Port {port} is open")
    s.close()
