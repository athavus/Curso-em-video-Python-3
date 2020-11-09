n = list()
for c in range(0, 9):
    n.append(int(input(f'Digite o valor que você quer colocar na posição {c}: ')))
print()
for c in range(0, 9):
    print(f'[ {n[c]:^5} ]', end='')
    if c == 2 or c == 5 or c == 8:
        print('\n')
