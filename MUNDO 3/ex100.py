from random import randint
from time import sleep


def mostraLinha(texto):
    """mostraLinha
    Mostrar uma linha formatada com um texto envolto a elas

    Parâmetros:
        texto [tipo(string)]: [Esse será o texto que irá ficar formatado em volta das linhas
        com 50 espaços centralizados]
    """    
    print()
    print('=' * 50)
    print(texto.center(50))
    print('=' * 50)


def sorteia(numeros):
    """sorteia
    Faz o sorteio de 5 números inteiros entre 1 e 10 e coloca dentro de uma lista chamada numeros
    Parâmetros:
        numeros (lista/array): [Esta será a lista que iremos colocar os números sorteados pelo
        módulo random e comando randint]
    """    
    mostraLinha('SORTEIO DOS NÚMEROS')
    print(f'Foram sorteados os números: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ')
        sleep(0.2)
    print()


def somaPar(numeros):
    """somaPar
    Esta def faz a soma de todos os números pares da lista randômica feita anteriormente pela função
    sorteia
    Parâmetros:
        numeros (lista/array): [Essa é a lista com os números já sorteados que serão manipulados pela
        função somaPar]
    """    
    mostraLinha('SOMA DOS NÚMEROS PARES')
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(f'A soma de todos os valores pares sorteados foi: {s}')


num = []
sorteia(num)
somaPar(num)
