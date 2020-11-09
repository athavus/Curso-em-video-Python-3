total = []
par = []
impar = []
while True:
    print('=' * 30)
    numero = int(input('Digite um número: '))
    print('=' * 30)
    total.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
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
print(f'A lista com todos os números é {total}')
print(f'A lista dos números pares é {par}')
print(f'A lista dos números ímpares é {impar}')
