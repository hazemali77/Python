#!/usr/bin/python3.6
import socket
import re

# family = Internet, Type= stream socket means TCP
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.db.no", 80))

http_get = b"GET / HTTP/1.1\nHost: www.db.no\n\n"
data=''

try:
    sock.sendall(http_get)
    data=sock.recvfrom(1024)
    
except socket.error:
    print(" Socket error", socket.errno)
finally:
    print("Closing connection")
    sock.close()
    
    
strdata=data[0].decode("utf-8")
headers=strdata.splitlines()
for s in headers:
    if re.search('Server:', s):
        s.replace("Server: ", "")
        print(s)
        print(data)