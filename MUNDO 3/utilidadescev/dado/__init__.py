def leiadinheiro(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = float(num)
            break
        else:
            print('\033[1;31mERRO! Você não digitou um número inteiro, tente novamente.\033[m')
    return num
