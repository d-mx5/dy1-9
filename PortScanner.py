#!/usr/bin/python3

#importing the socket package
import socket
#https://docs.python.org/3/library/socket.html

#defining the socket variable "S" and then specifying that we are using IPV4 (AF_INET) and then TCP (sock_Stream)
#Socket family is used to specify the protocol for communication. IPv4 is AF_INET and Ipv6 is AF_INET6
#Socket type depends on the protocol we are using. TCP is sock_stream and UDP is sock_degram

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

#defining the variables of the host and port by prompting the user to make a selection
host = input("Please enter an IP Address:")
port = int(input("Please enter the port you want to scan:"))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)



