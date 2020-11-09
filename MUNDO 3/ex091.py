from random import randint
from operator import itemgetter
from time import sleep
jogadores = {'jogador 1': '', 'jogador 2': '', 'jogador 3': '', 'jogador 4': ''}
for c in range(0, 4):
    a = randint(1, 6)
    sleep(1)
    print(f'O jogador {c+1} tirou {a}')
    jogadores[f'jogador {c+1}'] = a
dados = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
print()
print('=' * 30)
print('RESULTADOS'.center(30))
print('=' * 30)
print()
for c in range(0, 4):
    sleep(1)
    print(f'{c+1}ª O {dados[c][0]} com {dados[c][1]}') 
