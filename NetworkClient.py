#!/usr/bin/python3.6
import socket

host='centos'

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host, 8070)
mysock.connect(addr)

try:
    msg=b"Hello\n"
    mysock.sendall(msg)
except socket.errno as e:
    print(" Socket error", e)
finally:
    mysock.close()  
  

