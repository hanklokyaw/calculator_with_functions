def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


print("Welcome to calculator app!")
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

old_record = False
continue_calculation = True

while continue_calculation:
    if not old_record:
        num1 = float(input("Enter the first number: "))
    for operator in operators:
        print(operator)
    symbol = input("choose an operator: ")
    num2 = float(input("Enter the second number: "))

    cal_function = operators[symbol]
    result = cal_function(num1, num2)

    print(f"{num1} {symbol} {num2} = {result}")
    new_record = input(f"Enter 'y' continue with current result {result} or 'n' to start a new calculation?").lower()
    if new_record == 'y':
        old_record = True
        num1 = result
    elif new_record == 'n':
        old_record = False
        num1 = 0
    else:
        print("Wrong enter please try again!")