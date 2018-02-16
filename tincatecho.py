#!/usr/bin/python3.6
import socket

#size=512
host=''
port=9898



def create_listen_socket(host, port) :
  # setup the sockets our server will recieve connection requests on
  ## family = Internet, Type= stream socket means TCP
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # We have a socket, we need to t bind to an IP address and port
    #to have a a place to listen on.

    sock.bind((host,port))
    sock.listen(100)
    return sock
# We can store informatin aboutthe other end
#once we accept the connecion attempt
def recv_msg(sock) :
    """
    Wait for data to arrive on the socket, 
    then parse into message using b'\0\'
    """
    data=bytearray()
    msg=''
    """Repeatedly read 4096 bytes off the socket, 
    storing the bytes into data until we see a delimiter
    """
    while not msg:
        recvd=sock.recv(4096)
        if not recvd:
	    # Socket has been closed prematurely raise connectionError()
	    raise ConnectionError()
	data=data+recvd
	if b'\0' in recvd:
	  '''
	  we know from our protocol rules that we only send
	  one message per connection, so b'\0' will always be the last ch.
	  '''
	  msg=data.rstrip(b'\0')
    msg=msg.decode('utf-8')
    return msg
    
def prep_msg(msg):
    """ prepare a string to be sent as a messag"""
    msg += '\0'
    return sg.encode('utf-8')

def send_msg(sock, msg):
    # send a string over a socket
    data=prep_msg(ms)
    sock.sendall(msg)
  


