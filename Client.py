import socket

HEADER = 16
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = '.EXIT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

