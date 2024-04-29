import socket

host = "localhost"
port = 6001

s = socket.socket()
s.connect((host, port))

with open("test.xlsx", 'wb') as f:
    print("File opened.")

    while (True):
        print("Receiving data...")
        data = s.recv(1024 * 16)

        if not data:
            break
        
        f.write(data)

    f.close()
    print("File successfully transfered!")

    s.close()
    print("connection closed.")
    