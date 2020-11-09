a = []
for c in range(0, 5):
    b = int(input('Digite um número: '))
    for posicao, valor in enumerate(a):
        if b < valor:
            a.insert(posicao, b)
            break
    else:
        a.append(b)
print(a)
