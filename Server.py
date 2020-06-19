import socket
import threading

FORMAT = 'utf-8'
HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MSG = '.EXIT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def start():
    server.listen()
    print("LISTENING ON ", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("\nACTIVE CONNECTIONS: ", threading.activeCount() - 1)


def handle_client(conn, addr):
    print(addr, "\nconnected...")
    Connected = True
    while Connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(addr, ": ", msg)

            if msg == DISCONNECT_MSG:
                Connected = False

    conn.close()

print("[STARTING]")
start()

