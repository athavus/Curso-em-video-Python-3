dt = float(input('Digite a distância da sua viagem em Km: '))
if dt > 200:
    km = 0.45 * dt
else:
    km = 0.50 * dt
print(f'O valor da passagem é R${km:.2f}')
