"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

import sys
from socket import *
from PythonCard import model
from Crypto.Cipher import AES
import hashlib
import string
import base64

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass

    def on_cmdSend_mouseClick(self, event):
        #Get IP address of the remote system
        #Define port
        remote_ip = self.components.txtAddr.text
        serverHost = remote_ip
        serverPort = 5000

        #Create TCP socket
        s = socket(AF_INET, SOCK_STREAM)

        #Connect to remote system
        s.connect((serverHost, serverPort))

        message = self.components.txtMsg.text
        length = 16 - (len(message) % 16)
        message += chr(length)*length

        #Get password and generate key as SHA256 digest
        Pass = self.components.txtKey.text
        encodedPass = hashlib.sha256(Pass).digest()

        #Encrypt function
        EncryptData = AES.new(encodedPass, AES.MODE_ECB)
        ciphertext = EncryptData.encrypt(message)

        s.send(base64.b64encode(ciphertext))

        #Send user input and wait for 1K reply packet
        s.send(self.components.txtMsg.text)
        self.components.txtStatus.text="Sending..."
        data = s.recv(1024)
        print data

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
