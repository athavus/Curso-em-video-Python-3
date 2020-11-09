s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print(f'A soma de todos os números ímpares no intervalo de 1 até 500 é {s}')
