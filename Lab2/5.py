print('Jaką operację chcesz wykonać?\n',
      '\t1) dodawanie\n', '\t2) odejmowanie\n',
      '\t3) mnożenie\n', '\t4) dzielenie\n',
      '\t5) potęgowanie')
wybor = int(input('Wpisz numer operacji: '))
if not(0 < wybor < 6):
    print('Niepoprawny numer operacji')
    exit()
try:
    zmienna1 = float(input('Podaj argument 1: '))
except:
    print('Niepoprawny argument')
    exit()
try:
    zmienna2 = float(input('Podaj argument 2: '))
except:
    print('Niepoprawny argument')
    exit()
if wybor == 1:
    wynik = zmienna1 + zmienna2
elif wybor == 2:
    wynik = zmienna1 - zmienna2
elif wybor == 3:
    wynik = zmienna1 * zmienna2
elif wybor == 4:
    '''if zmienna2 == 0:
        print('Nie można dzielić przez zero!!!')
        exit()
    '''
    try:
        wynik = zmienna1 / zmienna2
    except ZeroDivisionError:
        print('Nie można dzielić przez zero!!!')
        exit()
elif wybor == 5:
    wynik = zmienna1 ** zmienna2
print(f'Wynik: {wynik}')
