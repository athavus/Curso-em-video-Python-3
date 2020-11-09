a = float(input('Digite o preço do produto: R$'))
print('''\033[4mFORMAS DE PAGAMENTO\033[m'
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
b = int(input('Digite a opção de pagamento:'))
if b == 1:
    a = a * 0.90
elif b == 2:
    a = a * 0.95
elif b == 3:
    a = a
elif b == 4:
    a = a * 1.20
else:
    print('\033[1;31mErro\033[m! A condição de pagamento que você colocou não existe.')
print(f'O novo preço do produto é \033[32m{a:.2f}\033[m!')
