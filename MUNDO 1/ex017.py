from math import sqrt
c1 = float(input('Insira o valor do cateto oposto em cm: '))
c2 = float(input('Insira o valor do cateto adjacente em cm: '))
hipo = c1 ** 2 + c2 ** 2
print(f'O comprimento da hipotenusa é {sqrt(hipo):.1f}cm')
