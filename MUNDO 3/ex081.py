a = []
cont = 0
while True:
    a.append(int(input('Digite um número: ')))
    cont += 1
    while True:
        stop = input('Você quer continuar? [S/N] ').upper()[0]
        if stop == 'S' or stop == 'N':
            break
        else:
            print('Você não escolheu uma opção válida.')
    if stop == 'S':
        continue
    elif stop == 'N':
        break
print(f'\nForam digitados {cont} números!')
a.sort(reverse=True)
print(a)
if 5 in a:
    print('O número 5 se encontra na lista')
else:
    print('O número 5 não se encontra na lista')
