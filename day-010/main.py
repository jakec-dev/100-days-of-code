from art import logo
from os import system

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    system("clear")
    print(logo)
    num1 = float(input("What's the first number?: "))

    continue_calculating = True
    while continue_calculating:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
        if should_continue == "n":
            continue_calculating = False
            calculator()
        else:
            num1 = answer
            
calculator()