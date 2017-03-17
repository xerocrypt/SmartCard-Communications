#!/usr/bin/python
#Client program for communicating with the live server
#Michael, 2014

import sys
from socket import *

#Get IP address of the remote system
#Define port
remote_ip = raw_input("IP ADDRESS: ")
serverHost = remote_ip
serverPort = 5000

#Create TCP socket
s = socket(AF_INET, SOCK_STREAM)

#Connect to remote system
s.connect((serverHost, serverPort))

#Send user input and wait for 1K reply packet
s.send(raw_input("MESSAGE: "))
print "Sending..."
data = s.recv(1024)
print data
