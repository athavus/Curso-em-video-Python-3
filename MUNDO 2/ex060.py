a = int(input('Digite um número para ver o seu fatorial: '))
b = 1
print(f'Calculando {a}!', end=' = ')
while a > 1:
    print(f'{a}', end=' x ')
    a = a - 1
    b += b * a
print(f'1 = {b}')
