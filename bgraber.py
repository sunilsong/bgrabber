#!/usr/bin/python
import sys
import socket

def portscan(host, port):
	socket.setdefaulttimeout(3)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print "connecting to the target"
		s.connect((host, port))
	except Exception as e:
		print str(e) + " : port might be closed"
	s.send("just grabbing your banner")
	print "waiting to receive reply"
	try:
		banner = s.recv(128).strip("\n")
	except Exception as e:
		print str(e) + " : service not available."
	else:
		s.close()
		return banner

def main():
	if (len(sys.argv) < 3) or (len(sys.argv) > 3):
		print "use this format, #python bgrabber.py <host> <ports>. if multiple ports use comma separated"	
		exit(0)
	else:
		host = sys.argv[1]
		if (host.isalpha() is True):
			try:
				host = socket.gethostbyname(host)
				print "target: " + host
			except Exception as e:
				print e
				exit(0)
		else:
			ports = sys.argv[2].split(',')
			for port in ports:
				try:
					banner = portscan(host, int(port))
				except Exception as e:
					print str(e) + ", jpt value halne?"
				else:
					if (banner is None):
						print "no banner captured"
					else:
						print "Banner on port: " + port + " = " + banner + "\n"
		exit(0)

if __name__ == '__main__':
	main()
