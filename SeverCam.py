import socket 
import threading 
import uuid
import os

HEADER=64 
PORT=5050 
SERVER=socket.gethostbyname(socket.gethostname()) 
ADDR=(SERVER, PORT) 
FORMAT='utf-8' 
DISCONNECT_MESSAGE='!DISCONNECT' 

clients, names=[], [] 
file = str(uuid.uuid4())                
server=socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM) 

server.bind(ADDR) 

class Comm:
    def __init__(self):
        self.file = file

    def start(self):
        print(f'[LISTENING] Server is listening on {SERVER}') 
        server.listen() 

        while True: 
            conn, addr=server.accept() 
            conn.send('Name'.encode(FORMAT)) 
            name_length=conn.recv(HEADER).decode(FORMAT) 
            name_length=int(name_length) 
            name=conn.recv(name_length).decode(FORMAT)
            names.append(name) 
            clients.append(conn) 

            print(f'Name is: {name}') 
            conn.send('Connection successful!'.encode(FORMAT)) 

            thread=threading.Thread(target=self.handle, 
                                      args=(name, conn, addr)) 
            thread.start() 

            print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}') 

    def handle(self, name, conn, addr): 
        _addr=str(addr).split(', ')[0] 
        _addr=_addr.replace('(', '') 
        _addr=_addr.replace('\'', '') 

        print(f'[NEW CONNNECTION] {_addr} connected.') 

        connected=True 
        while connected: 
            message_length=conn.recv(HEADER).decode(FORMAT) 
            message_length=int(message_length) 
            message=conn.recv(message_length) 

            if message.decode(FORMAT) == DISCONNECT_MESSAGE: 
                clients.remove(conn) 
                names.remove(name) 
                print(f'Name is: {name}') 
                print(f'[DISCONNECT] {_addr} disconnected') 
                connected=False
            else:
                path = os.path.dirname(__file__)
                fileP = f'{path}/{self.file}.png'
                file = open(fileP, 'a')
                file.write(message.decode(FORMAT))

        conn.close() 

print('\n[STARTING] Server is starting...') 
comm = Comm()
comm.start() 
