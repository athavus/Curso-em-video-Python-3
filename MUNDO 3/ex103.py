def ficha(nome='', gols=0):
    """Ficha

    Parâmetros:
        nome (string): Nome do jogador
        gols (int, optional): Gols marcados pelo jogador. Defaults to 0.

    Returns:
        lista: Lista com o nome do jogador e o tanto de gols que o mesmo fez
    """    
    print('-' * 50)
    if len(nome) == 0:
        nome = '<desconhecido>'
    lst = nome, gols
    return lst


print('-' * 50)
a = input('Jogador: ').strip().capitalize()
b = input('Digite o números de gols que o jogador marcou: ').strip()
if b.isnumeric():
    b = int(b)
else:
    b = 0
jogador = ficha(a, b)
print(f'O jogador {jogador[0]} marcou {jogador[1]} gols')
