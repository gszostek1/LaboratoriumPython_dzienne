# Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
# mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.
# Np. Wejście: 10, 5
# Wyjście: 5, 6, 7, 8, 9, 10

a=int(input("Proszę podać a "))
b=int(input("Proszę podać b "))
if a > b:
    a, b = b, a
while a <= b:
    print(a, end=" ")
    a += 1