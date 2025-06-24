import socket
import time

#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind(('', 8892))
#become a server socket
serversocket.listen(1)

time.sleep(30)

print 'done listening'
