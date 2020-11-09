a = input('Digite uma frase para ver se é um palíndromo: ').upper()
b = a.split()
c = ''.join(b)
d = ''
for letra in range(len(c) - 1, -1, -1):
    d += c[letra]
if d == c:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
