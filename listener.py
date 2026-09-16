import socket

from connection import Connection


class Listener:
    def __init__(self, host, port, backlog =1000):
        #Assigns values to Listener object  
        self.host = host
        self.port = port
        self.backlog = backlog
        self.con= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __repr__(self):
        return f'Listener(port={self.port}, host={self.host}, backlog={self.backlog})'

    def start(self):
        self.con.bind((self.host , self.port))
        self.con.listen(self.backlog)

    def stop(self):
        self.con.close()

    def accept (self):
        while True:
            new_con= self.con.accept()
            return Connection(new_con)

        

