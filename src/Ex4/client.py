# Import modules/libs
import xmlrpc.client

# Connect to server via an address
server = xmlrpc.client.ServerProxy('http://localhost:8005')

print("Operations with two integer numbers.")

while (True):
    try:
        # Input for two integer numbers
        num1 = int(input("\nType first number: "))
        num2 = int(input("Type second number: "))

        # Call specific server functions and print the result on screen
        print(f"\nSum ({num1} + {num2}): ", server.add(num1, num2))
        print(f"Times ({num1} x {num2}):", server.times(num1, num2))
        print(f"Power ({num1}^{num2}):", server.pow(num1, num2))
        print(f"Division ({num1} / {num2}):", server.div(num1, num2))
        print(f"Subtraction ({num1} - {num2}):", server.sub(num1, num2))
    except:
        # Write an error message if no integer number was provided by the inputs
        print("Please, provide only integer numbers.")        

    # Ask the user whether the program should continue or not. Only Y or N valid
    message = input("\nDo you wish to continue? (Yes / No) ")
    message = message.upper().strip()[0]
        
    # If the user doesn't want to continue, break out of the loop and finish the program
    if (message == 'N'):
        break
