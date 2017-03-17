#!/usr/bin/python
#Server program for accepting client messages
#Michael, 2014

import socket
import sys
 
#Listen on port 5000
HOST = ''
PORT = 5000

#Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind to socket unless error
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'STATUS: Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
s.listen(10)
print 'STATUS: Server is running.'
 
#Keep listener running and respond to incoming packet
while 1:

    conn, addr = s.accept()
    print 'STATUS: Incoming connection from ' + addr[0] + ':' + str(addr[1])
    data = conn.recv(1024)
    reply = 'Recieved.' + data
    print data
    if not data:
        break
     
    conn.sendall(reply)
 
#Close connection and close socket
conn.close()
s.close()
