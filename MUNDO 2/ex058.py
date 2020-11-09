from random import randint
a = randint(0, 10)
print('-=-' * 11)
print('Será que você consegue me vencer?')
print('-=-' * 11)
b = int(input('Tente acertar o número que o computador pensou (entre 0 e 10): '))
cont = 1
while b != a:
    print('ERRADO!')
    if b > a:
        b = int(input('Menos... Tente outro número (entre 0 e 10): '))
    elif a > b:
        b = int(input('Mais... Tente outro número (entre 0 e 10): '))
    cont += 1
print(f'ACERTOU! \nVocê precisou de {cont} tentativas para acertar o número que o computador pensou!')
