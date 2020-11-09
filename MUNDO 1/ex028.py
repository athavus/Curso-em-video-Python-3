from random import randint
from time import sleep
a = randint(0, 5)
print('-=-' * 11)
print('Será que você consegue me vencer?')
print('-=-' * 11)
b = int(input('Tente acertar o número que o computador pensou (entre 1 e 5): '))
print('PROCESSANDO NÚMERO...')
sleep(3)
if a == b:
    print(f'PARABÉNS! Você ganhou, o número era {a}')
else:
    print(f'ERRADO! O computador venceu, o número era {a}')
