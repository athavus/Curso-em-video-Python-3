from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
anoatual = date.today().year
cont = (anoatual - ano)
if cont < 18:
    print('Você ainda vai se alistar ao serviço de alistamento!')
    print(f'Faltam {18 - cont} anos para você se alistar')
elif cont == 18:
    print('É a hora de se alistar ao serviço de alistamento!')
else:
    print('Já passou da hora de se alistar ao o seviço de alistamento!')
    print(f'Já passaram {cont - 18} anos do tempo que você deveria se alistar')
