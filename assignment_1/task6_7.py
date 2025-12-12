num1 = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0: #task7
        result = num1 / num2
    else:
        result = "Err"
else:
    result = "Err"
print(f"{num1} {op} {num2} = {result}")
