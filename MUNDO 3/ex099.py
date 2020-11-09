from time import sleep


def maior(* num):
    """maior
    Essa função mostra o maior número de uma lista
    """    
    print('-=' * 40)
    print('Analisando os valores passados...')
    for c in num:    
        print(c, end=' ')
        sleep(0.2)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(num)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
