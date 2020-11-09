jogador = {}
jogador['Nome'] = input('Digite o nome do jogador: ')
jogador['Partidas'] = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou: '))
gols = 0
for c in range(0, jogador['Partidas']):
    jogador[f'Gol{c}'] = int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}ª partida: '))
    gols += jogador[f'Gol{c}']
print()
print('=' * 40)
print(f'Resultados de nome {jogador["Nome"]}'.center(40))
print('=' * 40)
for c in range(0, jogador['Partidas']):
    print(f'Na {c + 1}ª partida, {jogador["Nome"]} fez {jogador[f"Gol{c}"]} gol(s)')
print(f'\n{jogador["Nome"]} fez nas suas {jogador["Partidas"]} partidas, {gols} gols!')