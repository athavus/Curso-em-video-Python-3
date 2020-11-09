maior = 0
menor = 0
for c in range(0, 5):
    a = float(input('Digite o seu peso: '))
    if c == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print(f'\nO maior dos pesos lidos foi {maior}Kg e o menor dos pesos lidos foi {menor}Kg!')
