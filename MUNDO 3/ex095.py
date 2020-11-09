jogador = {}
total = []
while True:
    jogador['Nome'] = input('Digite o nome do jogador: ')
    jogador['Partidas'] = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou: '))
    gols = 0
    for c in range(0, jogador['Partidas']):
        jogador[f'Gol{c}'] = int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}ª partida: '))
        gols += jogador[f'Gol{c}']
    jogador['Todos os gols'] = gols
    total.append(jogador.copy())
    stop = str(input('Você quer continuar? [S/N] '))
    if stop in 'Nn':
        break
print()
print('=' * 75)
print(f'APROVEITAMENTO DOS JOGADORES'.center(75))
print('=' * 75)
print(f'{"POSIÇÃO"} | {"NOME":.<30} | {"PARTIDAS JOGADAS"} | {"GOLS TOTAIS"} |')
for pos, c in enumerate(total):
    print(f'{pos + 1:.<7} | {total[pos]["Nome"]:.<30} | {total[pos]["Partidas"]:>16} | {total[pos]["Todos os gols"]:>11} |')
while True:
    nota = int(input('\nDigite a posição do jogador que você deseja ver o aproveitamento: [999 para encerrar] '))
    if nota == 999:
        break
    for pos, c in enumerate(total):
        if nota - 1 == pos:
            print(f'\nO aproveitamento do jogador(a) {total[pos]["Nome"]} nas suas {total[pos]["Partidas"]} partidas foi:')
            for c in range(0, total[pos]['Partidas']):
                print(f'{c + 1}ª partida: {total[pos][f"Gol{c}"]} gols')
print('EXECUÇÃO ENCERRADA!')
