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

def send_file_to_client(filename, connection):
    print("\nSending file to client...")

    # Open specified file as read binary mode
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

def receive_and_update_file(filename, connection):
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

while (True):
    # Try to accept a new client connection
    try:
        connection, address = s.accept()
        print("Connected by:", address)
    except:
        # Otherwise just skips to the next iteration
        continue

    # Define the file name and send its content to the client
    filename = "FT_test.txt"
    send_file_to_client(filename, connection)

    # Wait time for file changes on client side
    time.sleep(5)

    # Receive updated file from the client and overwrites the root file with new updated content
    receive_and_update_file(filename, connection)
    
    # Close connection with the client
    connection.close()
    print("\nConnection closed.\n")
