# Client Project
# DWP Moonen
#!/usr/bin/python3.6
import socket
from time import sleep

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.100.50"
port = 5150

server.connect((host, port))
data = server.recv(1024)
print(bytes.decode(data))

while True:
    data = input("Txt Pls : ")
    server.send(str.encode(data))
    data = server.recv(1024)
    print("Recv from Server : ", bytes.decode(data))
    if(bytes.decode(data) == "exit"):
        break

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
