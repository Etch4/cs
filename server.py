#!/usr/bin/python3.5

import socket
from time import sleep

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5150

server.bind((host, port))
server.listen(5)
print("Listening ...")
client, addr = server.accept()
print("client")
print("address")
print("Accept conn from: ", addr)
client.send(str.encode("Welcome to my Server"))

while True:
    data = client.recv(1024)
    if(bytes.decode(data) == "exit"):
        break
    else:
        print("Recv data from client :", bytes.decode(data))
        client.send(data)

client.send(str.encode("exit"))
server.close()
print("\n\n Connection is Closing ", end='')
sleep(.5)
print(".", end='', flush=True)
sleep(.5)
print(".", end='', flush=True)
sleep(.5)
print(".", end='', flush=True)
sleep(.5)
print("\n\n")

exit(0)
