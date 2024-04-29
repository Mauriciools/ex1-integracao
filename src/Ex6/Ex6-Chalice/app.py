# Import modules/libs
from chalice import Chalice
import requests

# Define the API URL
API_URL = "https://mrl0vy3w26.execute-api.sa-east-1.amazonaws.com/api/"

# Define chalice app
app = Chalice(app_name='Ex6-Chalice')

@app.route('/')
def index():
    # Ask the user which operation must be performed
    operation = input("Select the desired operation [soma] [sub] [mult] [div]: ").strip()

    try:
        # Ask the user two numbers to perform the desired operation
        num1 = int(input("Type the first number: "))
        num2 = int(input("Type the second number: "))
    except:
        # Write an error message if no integer number was provided by the inputs
        print("Please, provide only integer numbers.")

    # Perform request to the API based on the arguments passed by the user
    response = requests.get(API_URL + f"{operation}/{num1}/{num2}")

    # Print and return the response in json format
    print(response.json())
    return response.json()
