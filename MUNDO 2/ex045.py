# APRESENTAÇÃO DO JOGO
from random import choice, shuffle
from time import sleep
print('\033[1;30mVAMOS JOGAR PEDRA, PAPEL OU TESOURA!\033[m')

# ESCOLHA DA MÁQUINA
a = ['PEDRA', 'PAPEL', 'TESOURA']
shuffle(a)
computador = choice(a)

# ESCOLHA DO JOGADOR
player = input('Escolha entre \033[36mPEDRA\033[m, \033[33mPAPEL\033[m OU \033[31mTESOURA\033[m:\n').upper().strip()

# A COMPARAÇÃO DO JOGO ACONTECENDO E RESULTADOS
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

if player == 'PEDRA' or player == 'PAPEL' or player == 'TESOURA':
    if player == computador:
        print('\033[1;30m-=\033[m' * 5)
        print('\033[1;30mEMPATE!\033[m')
        print('\033[1;30m-=\033[m' * 5)

    elif (player == 'PEDRA' and computador == 'TESOURA') or (player == 'TESOURA' and computador == 'PAPEL') or \
            (player == 'PAPEL' and computador == 'PEDRA'):
        print('\033[1;32m-=\033[m' * 6)
        print('\033[1;32mVOCÊ GANHOU!')
        print('\033[1;32m-=\033[m' * 6)

    elif (player == 'PAPEL' and computador == 'TESOURA') or (player == 'PEDRA' and computador == 'PAPEL') or \
            (player == 'TESOURA' and computador == 'PEDRA'):
        print('\033[1;31m-=\033[m' * 10)
        print('\033[1;31mO COMPUTADOR GANHOU\033[m')
        print('\033[1;31m-=\033[m' * 10)
else:
    print('\033[31mVocê não escolheu pedra, nem papel, nem tesoura :(\033[m')
