def voto(ano=0):
    """Voto

    Parâmetros:
        ano (int, optional): Ano de nascimento da pessoa. Defaults to 0.

    Returns:
        array: Situação do voto e a idade da pessoa
    """
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        estado = 'VOTO OBRIGATÓRIO', idade
    elif 16 <= idade < 18 or idade >= 65:
        estado = 'VOTO OPCIONAL', idade
    elif idade < 16:
        estado = 'VOTO NEGADO', idade
    return estado
    

a = int(input('Digite o ano que você nasceu: '))
b = voto(a)
print(f'Voce têm {b[1]} anos: {b[0]}')
