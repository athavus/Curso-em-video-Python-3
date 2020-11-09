cont = s = 0
while True:
    n = int(input('Digite um número [999 para fechar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} números e a soma de todos eles foi {s}')
