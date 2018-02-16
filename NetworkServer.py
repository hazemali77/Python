#!/usr/bin/python3.6
import socket

size=512
host=''
port=9898

# family = Internet, Type= stream socket means TCP
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# We have a socket, we need to t bind to an IP address and port
#to have a a place to listen on.

sock.bind((host,port))
sock.listen(5)
# We can store informatin aboutthe other end
#once we accept the connecion attempt
c, addr=sock.accept()
data=c.recv(size)
msg=b"Hello2\n"
if data:
    f=open("storage.dat", '+w')
    print(" Connection from:", addr[0])
    f.write(addr[0])
    f.write(";")
    f.write(data.decode("utf-8"))
    f.close()
    
    c.sendall(msg)
sock.close()  
  


