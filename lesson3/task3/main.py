print("Квадратне рівняння: ax^2+bx+c=o")
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
c = int(input("Введіть значення c: "))
D = b**2 - 4 * a *c

if D > 0:
    x1 = (-b + (D**0.5)) / (2*a)
    x2 = (-b - (D**0.5)) / (2*a)
    print('x1 =',x1)
    print('x2 =',x2)
elif D == 0:
    x = -b/2*a
    print('x =',x)
else:
    print('Рівняння не має коренів')
input("Press to ENTER to exit")