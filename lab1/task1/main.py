a = float(input("Введіть число №1:"))
b = float(input("Введіть число №2:"))
c = input("Виберіть дію: -,+,*,/")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("Ділення на нуль ")