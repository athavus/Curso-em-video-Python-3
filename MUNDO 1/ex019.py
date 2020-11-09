from random import choice
n1 = input('Insira o nome do primeiro aluno: ')
n2 = input('Insira o nome do segundo aluno: ')
n3 = input('Insira o nome do terceiro aluno: ')
n4 = input('Insira o nome do quarto aluno: ')
a = [n1, n2, n3, n4]
escolhido = choice(a)
print(f'O aluno escolhido foi {escolhido}')
