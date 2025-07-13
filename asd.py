print("calculator on pythone")

num = float(input("Enter first number: "))
num1 = float(input("Enter secend number: "))

op = input("Enter operation, + - * / ")

if op == "+":
    print("result", num + num1)
    
elif op == "*":
    print("result", num * num1)

elif op == "-":
    print("result", num - num1)

elif op == "/":
    print("result", num / num1)

else:
    print("error")

