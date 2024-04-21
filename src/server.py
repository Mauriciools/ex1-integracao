# Import modules
from socket import *
from terminalColors import colors

# Define server address and port
host = '127.0.0.1'
port = 50009

# Instantiate socket object and start listening
socketObj = socket(AF_INET, SOCK_STREAM)
socketObj.bind((host, port))
socketObj.listen(1)

# Connects to a client
connection, address = socketObj.accept()
print('Server connected on:', address)

while True:
    # Receive and print the client's message
    data = connection.recv(1024)
    print(colors.OKCYAN + '\nClient sent:' + colors.ENDC, data.decode())

    # If message is 'fim' break out of the loop
    if (data.decode().upper().strip() == 'FIM'):
        break

    answer = ""

    # Write answer message to the client. 
    # The answer will only be sent if it's not empty 
    while (len(answer) == 0):
        print(colors.OKGREEN + 'Answer client message: ' + colors.ENDC)
        answer = input()

    # Send answer message to the client
    connection.send(answer.encode())
    
    # If the answer is 'fim' break out of the loop
    if (answer.upper().strip() == 'FIM'):
        break

# Close the connection
connection.close()
