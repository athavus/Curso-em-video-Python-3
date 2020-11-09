n = int(input('Digite um número [999 para parar]:'))
s = 0
cont = 0
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você parou! Foram digitados {cont} números e a soma de todos os números digitados foi {s}')
