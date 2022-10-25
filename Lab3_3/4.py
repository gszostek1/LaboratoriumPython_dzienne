x=int(input("Podaj liczbę"))
y=int(input("Podaj Liczbę"))
if y<x:
    x,y=y,x
while y>=x:
    print(x,end=" ")
    x = x + 1