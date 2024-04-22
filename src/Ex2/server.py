# Import modules/libs
import datetime
import random
import asyncio
import websockets

# Hello function for greeting a new user
async def hello(websocket, path):
    # Receives the user's name from the client
    name = await websocket.recv()
    print(f"< {name}")

    # Create a greetings message and send back to the client
    greeting = f" Hello {name}!"
    await websocket.send(greeting)
    print(f"> {greeting}")

# Time function to send two numbers to the server for adding them up
async def time(websocket, path):
    while True:
        try:
            print("\n")
            
            # Receives the first number to be added from the client
            num1 = float(await websocket.recv())
            print(num1)
            # Send acknowledge message back to the client
            await websocket.send("Server received number 1.")
            
            # Receives the second number to be added from the client
            num2 = float(await websocket.recv())
            print(num2)
            # Send acknowledge message back to the client
            # await websocket.send("Server received number 2.")

            # Verify if the numbers are int or float
            if (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
                # Send to the client a message containing the sum of both passed numbers
                await websocket.send(f"{num1} + {num2} = {num1 + num2}")

                # Random sleep
                await asyncio.sleep(random.random() * 3)
            else:
                # If the arguments are not int or float, send back to the client an error message
                await websocket.send("One of the arguments is not valid, please, enter only numbers.")
        except:
            # If any error occurred during operation, send back to the client an error message
            await websocket.send("One of the arguments is not valid, please, enter only numbers.")

        # Receives the final message from the client and send back an acknowledgement message
        message = await websocket.recv()
        await websocket.send("Received final message!")

# add_numbers function to send the result of the addition of two numbers to the client
async def add_numbers(websocket, path):
    while True:
        try:
            print("\n")
            
            # Ask the user for the first number to be added and send to the server
            num1 = float(input("Enter the first number to be added: "))
            
            # Ask the user for the second number to be added and send to the server
            num2 = float(input("Enter the second number to be added: "))

            # Verify if the numbers are int or float
            if (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
                # Send to the client a message containing the sum of both passed numbers
                await websocket.send(f"{num1} + {num2} = {num1 + num2}")

                # Random sleep
                await asyncio.sleep(random.random() * 3)
            else:
                # If the arguments are not int or float, send back to the client an error message
                await websocket.send("One of the arguments is not valid, please, enter only numbers.")
        except:
            # If any error occurred during operation, send back to the client an error message
            await websocket.send("One of the arguments is not valid, please, enter only numbers.")

        # Ask the user whether the program should continue or not. Only Y or N valid
        message = ""
        while ((len(message) == 0)):
            message = input("Do you wish to continue? (Yes / No) ")
            message = message.upper().strip()[0]
            
            # If the answer is different from Y (yes) or N (no)
            # set the message to empty so the program asks the user again
            if ((message != 'Y') and (message != 'N')):
                message = ""

        # If the user doesn't want to continue, break out of the loop
        if (message == 'N'):
            break

# Start the server on the specified address and port
start_server = websockets.serve(add_numbers, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
