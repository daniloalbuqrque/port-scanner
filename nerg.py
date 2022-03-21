import sys
import socket
import pyfiglet

version 1.0

def banner():
	banner = pyfiglet.figlet_format("NERG")
	print(banner)
	print("Created by github.com/daniloalbuqrque. Good dusk ツ\n")

banner()

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Usage: python3 nerg.py [target]")
	print("e.g.: python3 nerg.py 127.0.0.1")

print("=" * 50)
print("Scanning: " + target)
print("=" * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		conn = s.connect_ex((target, port))
		if conn == 0:
			print("{} - open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nStopping scan...")
	sys.exit()
except socket.gaierror:
	print("\nSomething went wrong with the hostname...")
	sys.exit()
except socket.error:
	print("\nThe server is not respoding...")
	sys.exit()


# scanning the services is missing yet
# scripts also missing
