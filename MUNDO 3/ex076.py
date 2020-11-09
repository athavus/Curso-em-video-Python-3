print('\033[1;31m=\033[m' * 40)
print(f'\033[1;31m{"PREÇO DOS PRODUTOS":^40}')
print('\033[1;31m=\033[m' * 40)
produto = 'Lápis', 3, 'Borracha', 2, 'Caderno', 20, 'Mochila', 40, 'Livros', 100, 'Corretivo', 5
for pos, c in enumerate(produto):
    if pos % 2 == 0:
        print(' {:.<30}'.format(c), end='')
    elif pos % 2 != 0:
        print(f'R${c:.2f}')
print('\033[1;31m=\033[m' * 40)
