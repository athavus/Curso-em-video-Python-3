a = int(input('Digite um número: '))
s = 0
s += a
mult = input('Você quer continuar digitando valores? ').lower().strip()
cont = 1
maior = menor = a
while mult != 'não':
    a = int(input('Digite um número: '))
    cont += 1
    s += a
    mult = input('Você quer continuar digitando valores? ').lower().strip()
    if a > maior:
        maior = a
    if a < menor:
        menor = a
print(f'A média dos números digitados foi {s / cont}\nO maior número digitado foi {maior} e o menor número foi {menor}')
