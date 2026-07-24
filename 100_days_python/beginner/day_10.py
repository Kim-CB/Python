# Functions with Outputs


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

math = {}
math["+"] = add
math["-"] = subtract
math["*"] = multiply
math["/"] = divide


# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
#print(math["*"](4,8))

def calculator():

    app_running = True
    while app_running:
        f_number = int(input("What's the first number?: "))
        should_continue = True
        while should_continue:
            operator = input("+\n-\n*\n/\nPick an operation: ")
            s_number = int(input("What's the next number?: "))
            operation = math[operator](f_number, s_number)
            print(f"{f_number} {operator} {s_number} = {operation}")
            continuar = input(f"Type 'y' to continue calculating with {operation}, or 'n' to stop , or 'stop' to really stop. ").lower()

            if continuar == "y":
                f_number = operation
            elif continuar == "n":
                app_running = False
            elif continuar == "stop":
                print("Thank you for calculating.")
                return

calculator()



