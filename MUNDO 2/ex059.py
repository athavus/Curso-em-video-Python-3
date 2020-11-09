a = int(input('\033[30mDigite um valor:\033[m '))
b = int(input('\033[30mDigite outro valor:\033[m '))
c = 0
while c != 5:
    print('''
    \033[1;30m[ 1 ]\033[m \033[1;31mSOMAR\033[m 
    \033[1;30m[ 2 ]\033[m \033[1;32mMULTIPLICAR\033[m
    \033[1;30m[ 3 ]\033[m \033[1;33mMAIOR\033[m
    \033[1;30m[ 4 ]\033[m \033[1;34mNOVOS NÚMEROS\033[m
    \033[1;30m[ 5 ]\033[m \033[1;35mSAIR DO PROGRAMA\033[m
    ''')
    c = int(input('\033[1;30mDigite a operação que você deseja fazer, correspondendo o menu:\033[m '))
    if c == 1:
        print(f'\033[31m\nA SOMA de {a} com {b} é igual a {a + b}!\033[m')
    elif c == 2:
        print(f'\033[32m\nO PRODUTO de {a} com {b} é igual a {a * b}!\033[m')
    elif c == 3:
        if a > b:
            print(f'\033[33m\nO MAIOR entre {a} e {b} é {a}!\033[m')
        else:
            print(f'\033[33m\nO MAIOR entre {a} e {b} é {b}!\033[m')
    elif c == 4:
        a = int(input('\033[34m\nDigite um novo valor:\033[m '))
        b = int(input('\033[34mDigite outro novo valor:\033[m '))
    else:
        print('\033[1;31mOpção INVÁLIDA!\033[m \033[1;30mTente novamente.\033[m')
    print('\033[1;30m=' * 40)
print('\033[1;32mOPERAÇÃO FINALIZADA!\033[m')
