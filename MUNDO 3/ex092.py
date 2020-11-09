from datetime import date
dados = {}
dados['Nome'] = input('Digite o seu nome: ')
dados['Ano'] = int(input('Digite o seu ano nascimento: '))
dados['CTPS'] = int(input('Digite a sua carteira de trabalho: [0 caso você não tenha carteira de trabalho] '))
idade =  date.today().year - dados['Ano']
if dados['CTPS'] != 0:
    dados['Trabalho'] = int(input('Digite o ano em que você foi contratado: '))
    dados['Salário'] = int(input('Digite o seu salário: '))
    aposentadoria = (dados['Trabalho'] - dados['Ano']) + 35
    print(f'O seu nome é: {dados["Nome"]}')
    print(f'A sua idade é: {idade}')
    print(f'A sua carteira de trabalho é: {dados["CTPS"]}')
    print(f'O seu salário é: R${dados["Salário"]}')
    print(f'Você irá se aposentar com: {aposentadoria} anos')
else:
    print(f'O seu nome é: {dados["Nome"]}')
    print(f'A sua idade é: {idade}')
