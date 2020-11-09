from datetime import date
anonascimento = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
ano = anoatual - anonascimento
if ano <= 9:
    print(f'Você tem {ano} anos e é um atleta da categoria \033[1;30mMIRIM\033[m!')
elif ano <= 14:
    print(f'Você tem {ano} anos e é um atleta da categoria \033[1;33mINFANTIL\033[m!')
elif ano <= 19:
    print(f'Você tem {ano} anos e é um atleta da categoria \033[1;36mJUNIOR\033[m!')
elif ano <= 25:
    print(f'Você tem {ano} anos e é um atleta da categoria \033[1;32mSÊNIOR\033[m!')
elif ano > 25:
    print(f'Você tem {ano} anos e é um atleta da categoria \033[1;35mMASTER\033[m!')
else:
    print('Erro! Idade não é válida')
