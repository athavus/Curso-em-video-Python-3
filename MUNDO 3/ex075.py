a = int(input('Digite mais um número:')),
int(input('Digite mais um número:')),
int(input('Digite mais um número:')),
int(input('Digite mais um número:'))
contpar = 0
if 9 in a:
    print(f'O número 9 apareceu {a.count(9)} vezes')
else:
    print('ERRO! Não temos o número 9 nos números digitados.')
if 3 in a:
    print(f'A primeira posição do número 3 foi {a.index(3) + 1}')
else:
    print('ERRO! Não temos nenhum número 3 nos números digitados')
print('Os números pares foram ')
for c in a:
    if c % 2 == 0:
        print(f'{c}', end=' ')
        contpar += 1
if contpar == 0:
    print('ERRO! Não foram digitados números pares')
else:
    print()
