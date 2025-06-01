def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def log_operation(operation, a, b, result):
    with open("log.txt", "a") as file:
        file.write(f"{a} {operation} {b} = {result}\n")

def calculator():
    print("Welcome to the Simple Calculator!")


    enable_logging = input("Do you want to enable logging? (yes/no): ").strip().lower()
    logging_enabled = enable_logging in ['yes', 'y']

