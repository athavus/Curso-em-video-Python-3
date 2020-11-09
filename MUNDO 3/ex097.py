def escreva(texto):
    """Texto com linhas

    Args:
        texto (string): Essa funcao centraliza uma string que ele receber com
        linhas em cima e embaixo
    """    
    print('~' * (len(texto) + 2))
    print(texto.center(len(texto) + 2))
    print('~' * (len(texto) + 2))


help(escreva)
