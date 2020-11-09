a = int(input('Digite um número: '))
conv = int(input('''Escolha o tipo de conversão que você deseja fazer.
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
\033[31mOperação: \033[m'''))
if conv == 1:
    print(f'O número {a} em binário é {bin(a)[2:]}')
elif conv == 2:
    print(f'O número {a} em octal é {oct(a)[2:]}')
elif conv == 3:
    print(f'O número {a} em hexadecimal é {hex(a)[2:]}')
else:
    print('Erro! Nenhuma opção foi selecionada, tente novamente')
