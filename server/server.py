import socket
import threading
import sys


HEADER = 4096
PORT = int(sys.argv[1])
SERVER = socket.gethostbyname(socket.gethostbyname("localhost"))
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DC = "SO LONG, SEE YOU LATER"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def start():
    server.listen()
    print(f"Server is [LISTENING] on {SERVER}\n")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Connections currently Active] {threading.active_count() - 1}\n")


def handle_client(conn, addr):
    print(f"[New connection Incoming] {addr} has connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DC:
                connected = False
            print(f"[{addr} has sent {msg}")
    conn.close()


print("[STARTING] server i215s starting.....")

start()

