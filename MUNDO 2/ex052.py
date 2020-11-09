a = int(input('Digite um número para ver se ele é primo: '))
mult = 0
for c in range(2, a):
    if a % c == 0:
        mult += 1
if mult == 0:
    print(f'{a} é um número primo!')
else:
    print(f'{a} não é um número primo!')
