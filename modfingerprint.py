import platform

def os_fingerprint():
  print(f"OS: {platform.system()} {platform.release()}"
