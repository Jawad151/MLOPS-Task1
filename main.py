from src.utils import add,sub,multiply,divide

if __name__ == "__main__":
    number1   = float(input("Enter Number 1: "))
    number2   = float(input("Enter Number 2: "))
    operation = input("Enter Operation: ")

    if operation == "+":
        print("Result: ",add(number1,number2))
    elif operation == "-":
        print("Result: ",sub(number1,number2))
    elif operation == "*":
        print("Result: ",multiply(number1,number2))
    elif operation == "/":
        print("Result: ",divide(number1,number2))
    else:
        print("Invalid Operation")
