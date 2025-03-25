import sys
from modules.recon import recon_scan
from modules.network_monitor  import monitor_network
from modules.debug import debug_client

def main();
  if len(sys.argv) < 2:
    print("Usage: python command_processor.py <command>")
    return

  command = sys.argv[1]

  if command == "recon":
    recon_scan()
  elif command == "monitor":
    monitor_network()
  elife command == "debug":
    debug_client()
  else:
    print("Unknown command")

if _name_ == "_main_";
  main()
