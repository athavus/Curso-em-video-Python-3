c = float(input('Digite o valor da casa: '))
s = float(input('Digite o valor do seu salário: '))
a = int(input('Quantos anos você quer pagar a casa? '))
p = c / (a * 12)
if p > (s * 0.30):
    print('\033[1;31mEMPRÉSTIMO NEGADO')
else:
    print('\033[1;32mEMPRÉSTIMO ACEITO')
