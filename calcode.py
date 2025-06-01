print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Exiting.")
        return

    if choice == '1':
        operation = '+'
        func = add
    elif choice == '2':
        operation = '-'
        func = subtract
    elif choice == '3':
        operation = '*'
        func = multiply
    elif choice == '4':
        operation = '/'
        func = dividedef add(a, b):
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
while True:
        try:
            a = float(input("\nEnter first number (or type 'exit' to quit): "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Exiting calculator.")
            break

        result = func(a, b)
        if result is None:
            continue

        print(f"Result: {result}")

        if logging_enabled:
            log_operation(operation, a, b, result)
            print("Operation logged.")


calculator()
