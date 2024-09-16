operator = input("Enter an operator (+, -, *, /): ")
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

if operator == '+':
    result = a + b
    print(result)
elif operator == '-':
    result = a - b
    print(result)
elif operator == '*':
    result = a * b
    print(result)
elif operator == '/':
    if b != 0:
        result = a / b
        print(result)
    else: 
        print("Error: learn some math \nyou can't divide something by 0.")
else:
    print("Invalid operator")
