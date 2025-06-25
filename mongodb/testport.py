import socket
IPs = ['10.227.242.242']
PORTs=[22,27017]

for IP in IPs:
   for PORT in PORTs:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((IP,PORT))
      if result == 0:
         print( f"Port {PORT} is open AT {IP}")
      else:
         print (F"Port {PORT} is NOT open AT {IP}")
      sock.close()
