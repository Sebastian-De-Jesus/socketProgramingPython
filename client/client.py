import socket
import sys

HEADER = 4096
PORT = int(sys.argv[2])
FORMAT = "utf-8"
DC = "SO LONG, SEE YOU LATER"
SERVER = "localhost"
#SERVER = sys.argv[1] would be used if we would bind to 137.151.27.1 which is ecs.fullerton.edu IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("TESTING BABY")
input()
send("TESTING BABY")
input()
send("TESTING BABY")
send(DC)

