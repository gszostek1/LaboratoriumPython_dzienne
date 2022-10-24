wiek = int(input('Wprowadź wiek klienta: '))
if wiek < 4:
    cena = 0
elif wiek < 18:
    cena = 10
else: cena = 20
print('Cena biletu:', cena, 'zł')
