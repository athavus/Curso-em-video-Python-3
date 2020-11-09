v = float(input('Insira a velocidade do carro: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você terá que pagar uma multa de R${multa:.2f} por exceder o limite de velocidade!')
print(f'Tenha um bom dia! Dirija com segurança!')
