a = []
while True:
    print('=' * 30)
    b = int(input('Digite um número: '))
    if b in a:
        a.remove(b)
    a.append(b)
    print('=' * 30)
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
a.sort()
print(a)
