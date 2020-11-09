print('=' * 30)
print('    PROGRESSÃO ARITMÉTICA')
print('=' * 30)
a = int(input('Digite o primeiro termo da progressão aritmética: '))
b = int(input('Digite a razão da progressão aritimética: '))
for c in range(0, 9):
    print(f'{a}', end=' ->')
    a = a + b
print(f'Acabou!')
