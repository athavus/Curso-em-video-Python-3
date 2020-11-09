dados = {}
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
elif dados['Média'] < 7:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}') 