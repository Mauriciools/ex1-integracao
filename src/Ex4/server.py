# Import modules/libs
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# RequestHandler class to define rpc paths
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Instantiate server object
with SimpleXMLRPCServer(('localhost', 8005), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Function to add two numbers
    def adder_function(x, y):
        print(x + y)
        return x + y
    
    # Function to multiply two numbers
    def multiplication_function(x, y):
        print(x * y)
        return x * y
    
    # Function to set x to the power of y
    def power_function(x, y):
        print(x ** y)
        return x ** y
    
    # Function to divide two numbers
    def division_function(x, y):
        # If the division is by 0, return an error message
        if (y != 0):
            print(x / y)
            return x / y
        else:
            print("Division by 0 is not possible.")
            return "Division by 0 is not possible."
    
    # Function to subtract two numbers
    def subtraction_function(x, y):
        print(x - y)
        return x - y
    
    # Register available functions with specific names that can be accessed by clients
    server.register_function(adder_function, 'add')
    server.register_function(multiplication_function, 'times')
    server.register_function(power_function, 'pow')
    server.register_function(division_function, 'div')
    server.register_function(subtraction_function, 'sub')
    server.serve_forever()
