def area():
    print('-' * 20)
    print('CONTROLE DE TERRENOS')
    print('-' * 20)
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    a = larg * comp
    print(f'A área do terreno de {larg}x{comp} é igual a {a}m²')


area()
