# Import modules/libs
import time
import socket
import datetime

# Define host and port
host = "localhost"
port = 6001

# Connect to the server using the address
s = socket.socket()
s.connect((host, port))
s.setblocking(0)

# Open specified file as write binary mode
with open("FT_file_received.txt", 'wb') as f:
    print("File opened.")

    time.sleep(1)

    while (True):
        print("Receiving data from server...")

        # Try to receive data from the server
        try:
            data = s.recv(1024 * 16)

            # If there is no data just goes out of the while loop
            if not data:
                break
        
            # Write existing data to file
            f.write(data)
        except:
            break      

    print("File successfully received!")

    print("\nUpdating file now...")

    # Define an update string and append to file
    updatedStr = f"\nUpdated by the client at {datetime.datetime.now()}"
    f.write(updatedStr.encode('utf-8'))

    # Close file
    f.close()
    print("File successfully updated!")

# Delay between updating file and sending back data to the server
time.sleep(1)
    
# Open specified file as read binary mode
with open("FT_file_received.txt", 'rb') as f:
    print("\nSending back data to the server...")

    # Read file content
    l = f.read(1024 * 16)

    # Iterates over the entire file content and send the corresponding data to the server
    while (l):
        s.send(l)
        l = f.read(1024 * 16)

    # Close file
    f.close()
    print("Updated file successfully sent back to the server!")

    # Close connection with the server
    s.close()
    print("\nConnection closed.")
