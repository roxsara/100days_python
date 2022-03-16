# Simple calculator
from art import logo


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
    print(logo)

    num1 = float(input("What\'s the first number? "))
    for symbol in operations:
        print(symbol)
    calculating = True

    while calculating:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What\'s the new number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        to_continue = input(f"Type 'y' to continue calculating with {answer},'n' for a new calculation or 'e' to exit:")
        if to_continue == 'y':
            num1 = answer
        else:
            calculating = False
            if to_continue == 'n':
                calculator()


calculator()