x = int(input("Enter the number"))

y = int(input("Enter the number"))

operation = input("Chose action +, -, *, /")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("error")