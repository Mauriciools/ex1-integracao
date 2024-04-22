# Import modules/libs
import asyncio
import websockets

# Define the server's address
address = 'ws://127.0.0.1:5678'

# Hello function for greeting a new user
async def hello():
    # Instantiate a websocket object by connecting to the server
    async with websockets.connect(address) as websocket:
        # Ask for the user's name
        name = input("What's your name? ")

        # Send the user's name to the server
        await websocket.send(name)
        print(f"> {name}")

        # Get the server's response and print 
        greeting = await websocket.recv()
        print(f"> {greeting}")

# Time function to send two numbers to the server for adding them up
async def time():
    # Instantiate a websocket object by connecting to the server
    async with websockets.connect(address) as websocket:
        while True:
            print("\n")

            # Ask the user for the first number to be added and send to the server
            num1 = input("Enter the first number to be added: ")
            await websocket.send(num1)
            response = await websocket.recv()

            # Ask the user for the second number to be added and send to the server
            num2 = input("Enter the second number to be added: ")
            await websocket.send(num2)
            response = await websocket.recv()

            # Ask the user whether the program should continue or not. Only Y or N valid
            message = ""
            while ((len(message) == 0)):
                message = input("Do you wish to continue? (Yes / No) ")
                message = message.upper().strip()[0]
                
                # If the answer is different from Y (yes) or N (no)
                # set the message to empty so the program asks the user again
                if ((message != 'Y') and (message != 'N')):
                    message = ""
                
            # Send message to the server
            await websocket.send(message)

            # If the user doesn't want to continue, break out of the loop
            if (message == 'N'):
                break
            
asyncio.get_event_loop().run_until_complete(time())
