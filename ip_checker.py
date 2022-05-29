import socket

value = True

while (value):
    url = input("Put URL addres: \n")

    ip = socket.gethostbyname(url)
    print (ip) 