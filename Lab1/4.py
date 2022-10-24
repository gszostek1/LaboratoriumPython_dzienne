znak = input('Wprowadź znak: ')
if znak >= 'a' and znak <= 'z':
    jaka = 'jest małą'
elif znak >= 'A' and znak <= 'Z':
    jaka = 'jest dużą'
else: jaka = 'znak nie jest literą'
print(f'Podany znak {jaka} literą')
