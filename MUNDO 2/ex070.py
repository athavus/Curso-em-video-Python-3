gasto = caro = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: '))
    gasto += p
    menor = p
    menornome = nome
    if p > 1000:
        caro += 1
    if menor > p:
        menor = p
        menornome = nome
    run = str(input('\033[30mVocê gostaria de continuar? [S/N]\033[m ')).upper().strip()
    if run[0] in 'S':
        print('\033[1;30mOk!\033[m\n')
    else:
        break
print(f'VALORES COMPUTADOS!')
print(f'O total gasto na compra foi R${gasto:.2f}')
print(f'{caro} produtos custaram mais de R$1000.00')
print(f'{menornome} é o nome do produto mais barato')
