x=-4
while x<=4:
    y=2*x**2-5*x-8
    if x == 2:
        x += 0.5
        continue
    print(f"f({x})={y}")
    x+=0.5

print("koniec")