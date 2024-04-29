import socket

host = "localhost"
port = 6001

s = socket.socket()
s.bind((host, port))
s.listen(1)

while (True):
    connection, address = s.accept()
    print("Connected by:", address)

    filename = "test.xlsx"
    f = open(filename, 'rb')
    l = f.read(1024 * 16)

    while (l):
        connection.send(l)
        l = f.read(1024 * 16)

    f.close()
    print("File sent!")
    
    connection.close()
    print("Connection closed.")
