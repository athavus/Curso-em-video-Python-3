dados = {}
totdados = []
mulher = []
maior = []
idade = cont = 0

while True:
    dados['Nome'] = input('Digite o seu nome: ')
    dados['Sexo'] = input('Digite o seu sexo: ').upper()
    dados['Idade'] = int(input('Digite a sua idade: '))
    if dados['Sexo'] in 'Ff':
        mulher.append(dados['Nome'])
    totdados.append(dados.copy())
    idade += dados['Idade']
    stop = input('Você quer continuar? [S/N] ')
    if stop in 'Nn':
        break

media = idade / len(totdados)
print()

print('=' * 40)
print('RESULTADOS'.center(40))
print('=' * 40)

print(f'\nForam cadastradas {cont} pessoas')

print(f'A média das idades de todos do grupo é {media:.2f}')

print('As mulheres do grupo são', end=': ')
for c in mulher:
    print(c, end=' ')

print('\nAs pessoas com idade acima da média são:')
for c in totdados:
    if c['Idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
        print()
