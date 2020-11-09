print('=' * 30)
print('    PROGRESSÃO ARITMÉTICA')
print('=' * 30)
a = int(input('Digite o primeiro termo da progressão aritmética: '))
b = int(input('Digite a razão da progressão aritimética: '))
cont = 1
while cont <= 10:
    print(f'{a}', end=' -> ')
    a = a + b
    cont = cont + 1
print('FIM!')
