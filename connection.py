import socket


class Connection:
    
    @classmethod
    def connect(cls, host, port):
        socky=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socky.connect((host, port))
        return cls(socky)
        #class method that creates a new connection to given host,port


    def __init__(self, connection: socket.socket):
        #give Connection a self.con function. 
        #now the socket is easily accessed
        self.con=connection
        self.ip, self.port = connection.getsockname()
        self.con_ip, self.con_port = connection.getpeername()


    def __repr__(self):
        return f'Connection from {self.ip}:{self.port} to {self.con_ip}:{self.con_ip}'

    
    def send_message(self, message: bytes):
        self.con.sendall(len(message.encode()).to_bytes(4, byteorder='little'))
        self.con.sendall(message.encode())
        #Sends message through socket


    def receive_message(self):  
        with self.con:
            l1=[]
            while True:
                data_len = self.con.recv(4)
                data_len = int.from_bytes(data_len, byteorder="little")
                data = self.con.recv(data_len)

                while len(data) < data_len:
                    data += self.con.recv(data_len - len(data))
                    if data[-data_len]== (b' '):
                        raise ConnectionResetError

                if not data:
                    break
                
                l1.append(data)
        return l1
        #Gets message from the connection
        #Throws an exception if connection is closed before we got the whole message

    def close(self):
        self.con.close()


