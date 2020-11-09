while True:
    n = int(input('\nDigite um número para ver a sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c:2}')
print('FIM!')
