def add(a,b):
    return a+b
def sub(a,b): 
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
print("This is a simple calculator tool.")
op = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if op == '+':
    result = add(num1, num2)
elif op == '-':
    result = sub(num1, num2)
elif op == '*':
    result = mul(num1, num2)
elif op == '/':
    result = div(num1, num2)
else:
    print("Invalid operation")
print(f"计算结果：{num1} {op} {num2} = {result}")