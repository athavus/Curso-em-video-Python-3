a = []
for c in range(0, 5):
    a.append(int(input('Digite um número: ')))
print(f'O maior valor da lista foi {max(a)}, nas posições ', end='')
for pos, c in enumerate(a):
    if c == max(a):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor da lista foi {min(a)}, nas posições ', end='')
for pos, c in enumerate(a):
    if c == min(a):
        print(f'{pos}...', end=' ')
