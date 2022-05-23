#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind((host, port))

#how many requests are allowed at a time
serversocket.listen(5)

while True:
    clientsocket, address = serversocket.accept()

    print("The connection has been recieved from " % str(address))

    message = 'Welcome to the server!' + "\r\n"
    clientsocket.send(message)
    
clientsocket.close

