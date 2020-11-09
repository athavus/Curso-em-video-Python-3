from random import shuffle
n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')
a = [n1, n2, n3, n4]
shuffle(a)
print(f'A ordem sorteada foi \n{a}')
