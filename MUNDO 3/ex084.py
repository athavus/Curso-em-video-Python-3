dados = list()
peso = list()
total = 0

while True:
    print('=' * 30)
    dados.append(input('Digite o seu nome: '))
    peso.append(float(input('Digite o seu peso: ')))
    print('=' * 30)
    total += 1
    stop = input('Você quer continuar? [S/N] ')[0]
    if stop in 'Nn':
        break

print(f'Foram cadastradas {total} pessoas!')

print(f'O maior peso foi {max(peso)}, do(s) usuário(s) ', end='')
for pos, c in enumerate(peso):
    if c == max(peso):
        print(f'{dados[pos]}...', end=' ')

print(f'\nO menor peso foi {min(peso)}, do(s) usuário(s) ', end='')
for pos, c in enumerate(peso):
    if c == min(peso):
        print(f'{dados[pos]}...', end=' ')
