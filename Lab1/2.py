import random
droga = random.randint(1,1000)

#droga =float(input('Podaj długość drogi przejechanej przez samochód (w km): '))
print(f'Długość drogi przejechanej przez samochód (w km): {droga}')
spal = float(input('Podaj średnie spalanie (w l/100km): '))
print(f"Przywidywane zużycie paliwa: {droga*spal/100} l")
print(f"Szacowany koszt podróży: {droga*spal/100*6.5} zł")
