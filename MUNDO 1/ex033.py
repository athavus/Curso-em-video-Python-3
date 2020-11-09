n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior número dentre os três é {maior}')
menor = n1
if n1 > n2 and n2 < n3:
    menor = n2
elif n1 > n3 and n3 < n2:
    menor = n3
print(f'O menor número dentre os três é {menor}')
