def aumentar(num=0, permais=0):
    novo_num = num + (num * (permais / 100))
    novo_num = moeda(novo_num)
    return novo_num


def diminuir(num=0, permenos=0):
    novo_num = num - (num * (permenos / 100))
    novo_num = moeda(novo_num)
    return novo_num


def dobro(num=0):
    num = num * 2
    num = moeda(num)
    return num


def metade(num=0):
    num = num / 2
    num = moeda(num)
    return num


def moeda(num=0):
    num = f'R${num:.2f}'
    return num


def resumo(num=0, permais=0, permenos=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(num)}')
    print(f'{"Dobro do preço:":<20}{dobro(num)}')
    print(f'{"Metade do preço:":<20}{metade(num)}')
    print(f'{f"{permais:.0f}% de aumento:":<20}{aumentar(num, permais)}')
    print(f'{f"{permenos:.0f}% de redução:":<20}{diminuir(num, permenos)}')
    print('-' * 30)
