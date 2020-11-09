def leiaInt(msg):
    """LeiaInt

    Returns:
        [int]: O retorno é o número que o jogador colocou dentro do nosso input.
    """    
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[1;31mERRO! Você não digitou um número inteiro, tente novamente.\033[m')
    return num


a = leiaInt('Digite um número: ')
print(f'Você digitou o número {a}!')
