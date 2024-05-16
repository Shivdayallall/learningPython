from art import logo
print(logo)

#Build a normal calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiple
}



def calculator():
    num1 = int(input("Enter first number: \n"))

    for symbol in operators:
        print(symbol)


    should_continue = True

    while should_continue:
        operation_symbol = input("Pick a operation from above: \n")

        num2 = int(input("Enter second number: \n"))

        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to continue with {answer} or no to start with new number: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

