import art

# TODO: Write out 4 functions - add(), subtract(), multiply() and divide().
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO : Create a dictionary called operations that contains the 4 operations as keys and the corresponding functions as values.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide   
}

# TODO : Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary and print the result.
#print(operations["*"](4, 8))

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}"  )

        choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()