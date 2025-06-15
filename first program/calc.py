def add(x, y):
        return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
def calculator():
    print("Welcome to the simple calculator! In which automation testing is also done.")
    print("enter your first number:")
    num1 = float(input())
    print("enter your second number:")
    num2 = float(input())
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter the number corresponding to your choice: ")
    if choice == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"The result of division is: {divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
