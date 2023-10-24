def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def main():
    print("Welcome to the Simple Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (+, -, *, /): ")

            if operation == '+':
                print(f"Result: {add(num1, num2)}")
            elif operation == '-':
                print(f"Result: {subtract(num1, num2)}")
            elif operation == '*':
                print(f"Result: {multiply(num1, num2)}")
            elif operation == '/':
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid operation. Please choose a valid operation.")
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == '__main__':
    main()
