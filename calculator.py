def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0: 
        return "Cannot divide by zero,try another number"
    return x/y
operation_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("Enter first number:"))
    for symbol in operation_dict:
        print(symbol)
        continue_cal=True
    while continue_cal:
        op_symbol=input("Pick an operation:")
        number2=float(input("Enter next number:"))
        cal_function=operation_dict[op_symbol]
        output=cal_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue=input(f"Enter 'c' to continue the calculation with {output} or Enter 'n' to start new calculation or Enter 'e' to exit calculation:")
        if should_continue=='c':
            number1=output
        elif should_continue=='n':
            continue_cal=False
            calculator()
        else:
            continue_cal=False
            print("Exiting calculator")
calculator()

