a = int(input("Proszę podać a "))
b = int(input("Proszę podać b "))
if a > b:
    a, b = b, a
while a <= b:
    print(a, end=" ")
    a += 1