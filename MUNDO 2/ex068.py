from random import randint
computador = randint(0, 10)
cont = 0
print('\033[1;31mVAMOS JOGAR ÍMPAR OU PAR!\033[m')
while True:
    escolhaplay = input('\033[30mimpar ou par? \033[m').lower().strip()
    print(f'\033[30mVocê escolheu {escolhaplay}\033[m')
    player = int(input('\033[30m\nDigite um número para jogar com o do computador: \033[m'))
    if (computador + player) % 2 == 0:
        win = 'par'
    else:
        win = 'impar'
    if escolhaplay == win:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
        cont += 1
    else:
        break
print(f'\033[1;31mVOCÊ PERDEU! Mas ganhou {cont} jogos seguidos, Parabéns!')
