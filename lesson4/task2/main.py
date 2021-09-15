n = int(input("Введіть число:"))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial )
input("Press ENTER to exit")