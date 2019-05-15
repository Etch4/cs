# Client Project
# DWP Moonen
#!/usr/bin/python3.6
import socket

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

print("Conn is Closing ...")
server.close()

exit(0)
