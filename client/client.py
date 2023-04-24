import socket
import sys
import os

HEADER = 2048
PORT = int(sys.argv[2])
FORMAT = "utf-8"
NOFILE = "FILE DOES NOT EXISIT"
DC = "GOODBYE"
SERVER = "localhost"

# SERVER = sys.argv[1] would be used if we would bind to 137.151.27.1 which is ecs.fullerton.edu IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Here our funciton simple formats the message to be sent to serverS
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

#In this function we follow the same syntax as above with slight modification because we are saving the
#recieved msg from the server, we additionaly are passing a filename to the function

def send_get_message(msg,filename):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #Response recieved from server saved in a variable we will use to confirm if file exit and we can write 
    #to our client floder
    recieved_response = client.recv(HEADER).decode(FORMAT)
    if recieved_response == NOFILE:
    	print(NOFILE)
    else:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory,filename)
        with open(file_path, 'w') as file:
            file.write(recieved_response)
    
connected = True
while connected:

    command = input("ftp> ".split())
    
    if len(command) == 0:
        continue
    # allows user to exit with the following quit command
    if command == "quit":
        send(DC)
        print(f"!!!!![DISCONNECTING] from {sys.argv[1]}!!!!!")
        break
    # allows users to list the conntents of CWD
    elif command == "ls":
        send(command)
        

    # Here we are sending over the command of get/pull which will be dealt with on the server side
    else:
        command_chosen = command.split()
        if command_chosen[0] == "get":
            send_get_message(command,command_chosen[1])





