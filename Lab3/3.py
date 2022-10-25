# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
# ujemnej, następuję wyjście z pętli.

while True:
    x = int(input('podaj liczbę: '))
    if x<0:
        break