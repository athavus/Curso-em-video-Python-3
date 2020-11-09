n = []
terceira = []
pares = []
for c in range(0, 9):
    n.append(int(input(f'Digite o valor que você quer colocar na posição {c}: ')))
    if n[c] % 2 == 0:
        pares.append(n[c])
print() 
for c in range(0, 9):
    print(f'[ {n[c]} ]', end='')
    if c == 2 or c == 5 or c == 8:
        terceira.append(n[c])
        print('\n')
print(f'A soma de todos os valores pares é igual a {sum(pares)}')
print(f'A soma de todos os valores da terceira coluna é igual a {sum(terceira)}')
print(f'O maior valor da segunda linha é {max(n[3:6])}')
