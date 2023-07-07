import socket


HEADER = 64
PORT = 55555
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECTED'
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length  = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('Hello World')
input()
send('I know socket programming')
input()
send('Jesus is lord')

send(DISCONNECT_MSG)

