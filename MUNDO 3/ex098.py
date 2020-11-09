from time import sleep


def contador(ini, fim, pas):
    """contador

    Anotações:
        ini (int): É o ínicio do intervalo para o contador
        fim (int): É o fim do intervalo para o for
        pas (int): É o passo do intervalo para o for
    """    
    print('=' * 30)
    if pas == 0:
        pas = 1
    if pas < 0:
        pas = pas * -1
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}:')
    if fim < ini:
        pas *= -1
        fim -= 1
    else:
        fim += 1
    for c in range(ini, fim, pas):
        print(c, end=' ')
        sleep(0.2)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, final, passo)
