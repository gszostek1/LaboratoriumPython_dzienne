# •	Dla osób poniżej 4 roku życia wstęp jest bezpłatny. (0; 4)
# •	Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł. [4; 18]
# •	Dla osób powyżej 18 roku życia bilet kosztuje 20zł. (18;
# Przykład: 	Wprowadź wiek klienta: 5
# 	Cena biletu: 10zł

wiek = int(input("Podaj wiek klienta: "))
if wiek < 4:
    cena = 0
elif wiek <= 18:
    cena = 10
else:
    cena = 20

print(f'Cena biletu: {cena}zł')
