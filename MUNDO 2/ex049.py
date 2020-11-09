a = int(input('Digite um número para ver a sua tabuada: '))
print('-=' * 8)
print(f'TABUADA DE {a}')
for c in range(1, 11):
    print(f'{a} X {c:2} = {a + c}')
print('-=' * 8)
