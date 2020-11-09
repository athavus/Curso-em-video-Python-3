valor = int(input('Digite quanto dinheiro você irá sacar: '))
total = valor
ced = 100
totced = 0
print('Você deverá sacar: ', end='')
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('VOLTE SEMPRE!')
