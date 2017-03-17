#!/usr/bin/python
#Client program for communicating with the live server
#Michael, 2014

import sys
from socket import *
from Crypto.Cipher import AES
import hashlib
import string
import base64

#Get IP address of the remote system
#Define port
remote_ip = raw_input("IP ADDRESS: ")
serverHost = remote_ip
serverPort = 5000

#Create TCP socket
s = socket(AF_INET, SOCK_STREAM)

#Connect to remote system
s.connect((serverHost, serverPort))

message = raw_input('MESSAGE: ')
length = 16 - (len(message) % 16)
message += chr(length)*length

#Get password and generate key as SHA256 digest
Pass = raw_input('KEY: ')
encodedPass = hashlib.sha256(Pass).digest()

#Encrypt function
EncryptData = AES.new(encodedPass, AES.MODE_ECB)
ciphertext = EncryptData.encrypt(message)
print base64.b64encode(ciphertext)

s.send(base64.b64encode(ciphertext))
print "Sending..."
data = s.recv(1024)
print data
