__author__ = 'hectormgerardo'

import socket
from requests import get

import socket

class connect():
    def __init__(self,y,z):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.y=y    # origin
        self.z=z    # destiny
    def wait4player(self):
        if self.y=='':
            self.y='127.0.0.1'
        self.serversocket.bind((self.z, 1111))
        self.serversocket.listen(1) # become a server socket
        while True:
            connection, address = self.serversocket.accept()
            buf = connection.recv(64)
            buf=buf.decode()
        return buf
    def lend(self,g):
        self.clientsocket.connect((self.z, 1111))
        self.clientsocket.send(bytes(g))
        #clientsocket.close()

#asdf=connect()
#asdf.lend()
#asdf.wait4player()
