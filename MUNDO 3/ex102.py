def fatorial(num=0, show=False):
    """Fatorial

    Parâmetro:
        num (int, optional): Valor para calcular o fatorial. Defaults to 0.
        show (bool, optional): Valor booleano para saber se iremos
        mostrar o processo de cálculo do fatorial ou não. Defaults to False.

    Returns:
        (int): Retorna o valor total do fatorial
    """    
    print('-' * 30)
    b = 1
    if show == True:
        while num > 1:
            print(f'{num}', end=' x ')
            num -= 1
            b += b * num
        print(f'1 =', end=' ')
    elif show == False:
        while num > 1:
            num -= 1
            b += b * num
    return b


a = int(input('Digite o número que você quer calcular o fatorial: '))
sit = input('Você quer ver o processo de cálculo do fatorial? [S/N] ')
if sit in 'Ss':
    sit = True
else:
    sit = False
print(fatorial(a, sit))
