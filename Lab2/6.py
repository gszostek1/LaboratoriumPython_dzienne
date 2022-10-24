znak = input('Wprowadź znak: ')
roznica = ord('A')-ord('a')

if 'a' <= znak <= 'z':
    znak = chr(ord(znak) + roznica)
    print(znak)
elif 'A' <= znak <= 'Z':
    znak = chr(ord(znak) - roznica)
    print(znak)
else:
    print('Wprowadzony znak nie jest literą.')
