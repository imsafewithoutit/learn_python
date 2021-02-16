a = float(input())
b = float(input())
func = str(input())

if func == "+":
    print(a + b)

elif func == "-":
    print(a - b)

elif func == "*":
    print(a * b)

elif func == "/":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)

elif func == "mod":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)

elif func == "pow":
    print(a ** b)

elif func == "div":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)
