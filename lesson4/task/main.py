a = int(input("Введіть число: "))
b = int(input("Введіть число: "))
total = 0
if a<=0:
    print("Некоректні дані")
elif b <= 0:
    print("Некоретні дані")
else:
    for i in range(a, b+1):
        total = total + i
        print(total)
input("Press ENTER to exit")

