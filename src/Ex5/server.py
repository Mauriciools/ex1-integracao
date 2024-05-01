# Import modules/libs
import time
import socket
import datetime

# Define host and port
host = "localhost"
port = 6001

# Configure server settings using socket
s = socket.socket()
s.bind((host, port))
s.listen(1)
s.setblocking(0)

while (True):
    # Try to accept a new client connection
    try:
        connection, address = s.accept()
        print("Connected by:", address)
    except:
        # Otherwise just skips to the next iteration
        continue

    print("\nSending file to client...")

    # Open specified file as read binary mode
    filename = "FT_test.txt"
    f = open(filename, 'rb')

    # Read file content
    l = f.read(1024 * 16)

    # Iterates over the entire file content and send the corresponding data to the client
    while (l):
        connection.send(l)
        l = f.read(1024 * 16)

    # Close file
    f.close()
    print("File successfully sent!")

    # Wait time for file changes on client side
    time.sleep(5)

    print("\nUpdating server's root file now...")

    # Open specified file as write binary mode
    f = open(filename, 'wb')
    print("File opened.")

    while (True):
        print("Receiving data from client...")

        # Try to receive data back from the client
        try:
            data = connection.recv(1024 * 16)

            # If there is no data just goes out of the while loop
            if not data:
                break
        
            # Write existing data to file
            f.write(data)
        except:
            break

    # Define an update string and append to file
    updatedStr = f"\nFile successfully updated in the server at {datetime.datetime.now()}"
    f.write(updatedStr.encode('utf-8'))
    
    # Close file
    f.close()
    print("File successfully updated on server side!")
    
    # Close connection with the client
    connection.close()
    print("\nConnection closed.\n")
