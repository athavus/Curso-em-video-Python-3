s = 0
for c in range(1, 7):
    a = int(input(f'Digite o {c}° número: '))
    if a % 2 == 0:
        s += a
print(f'A soma dos números pares que foram computados é {s}')
