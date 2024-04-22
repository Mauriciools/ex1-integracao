# Import modules
from socket import *
from terminal_colors import colors

# Define server address and port
host = '127.0.0.1'
port = 50009

# Instantiate socket object and connect to server
socketObj = socket(AF_INET, SOCK_STREAM)
socketObj.connect((host, port))

while True:
    # Write message to the server
    print(colors.OKCYAN + '\nType something: ' + colors.ENDC)
    message = input()

    # Do not proceed with the chat if the message is empty
    if (len(message) == 0):
        continue

    # Send message to the server
    socketObj.send(message.encode())

    # If the message is 'fim' break out of the loop
    if (message.upper().strip() == 'FIM'):
        break

    # Receive and print the server's message
    data = socketObj.recv(1024)
    print(colors.OKGREEN + 'Server replied:' + colors.ENDC, data.decode())

    # If the received answer is 'fim' break out of the loop
    if (data.decode().upper().strip() == 'FIM'):
        break

# Close connection to the server
socketObj.close()
