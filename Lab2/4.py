znak = input('Wprowadź znak: ')
if len(znak) > 1:
    print('Wprowadzono więcej niż jedną literę!')
    exit()
if 'a' <= znak <= 'z':
    print('Wprowadzono małą literę.')
elif 'A' <= znak <= 'Z':
    print('Wprowadzono dużą literę.')
else:
    print('Wprowadzony znak nie jest literą.')
