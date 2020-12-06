# 4 x 20

import socket 
import threading 

HEADER=64 
PORT=5050 
SERVER='192.168.1.8' 
ADDR=(SERVER, PORT) 
FORMAT='utf-8' 
DISCONNECT_MESSAGE='!DISCONNECT' 

client=socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM) 

while True: 
    try: 
        client.connect(ADDR) 
        break 
    except: 
        pass 
 
class Comm:
    def __init__(self, name):
        self.name = name

    def stop(self):
        while True:
            try:
                msg_length=len(DISCONNECT_MESSAGE) 
                send_length=str(msg_length).encode(FORMAT) 
                send_length += b' ' * (HEADER - len(send_length))
                client.send(send_length) 
                client.send(DISCONNECT_MESSAGE.encode(FORMAT)) 
            except ConnectionResetError:
                break

    def send(self, msg): 
        while True: 
            message=f'{self.name}: {msg}' 
            message=message.encode(FORMAT) 
            msg_length=len(message) 
            send_length=str(msg_length).encode(FORMAT) 
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length) 
            client.send(message) 
            break 

    def receive(self): 
        while True: 
            try:
                message=client.recv(1024).decode(FORMAT) 

                if message == 'Name': 
                    name=self.name.encode(FORMAT) 
                    name_length=len(name) 
                    send_length=str(name_length).encode(FORMAT) 
                    send_length += b' ' * (HEADER - len(send_length)) 
                    client.send(send_length) 
                    client.send(name) 
                else: 
                    return message
            except ConnectionResetError:
                break

    def start(self):
        rcv = threading.Thread(target=self.receive) 
        rcv.start() 
        self.receive()

comm = Comm('joani')
comm.start()
for _ in range(10001):
    comm.send(msg=f'Hi{_}')
comm.stop()
