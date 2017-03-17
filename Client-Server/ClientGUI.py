"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

import sys
from socket import *
from PythonCard import model

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

        #Send user input and wait for 1K reply packet
        s.send(self.components.txtMsg.text)
        self.components.txtStatus.text="Sending..."
        data = s.recv(1024)
        print data



if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
