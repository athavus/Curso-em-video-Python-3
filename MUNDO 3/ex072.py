extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', \
          'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', \
          'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    a = int(input('Digite o número que você deseja ver por extenso: (0 a 20) '))
    if not 0 <= a <= 20:
        print('Tente novamente. ', end=' ')
    print(f'Você digitou o número {extenso[a]}')
    b = input('Você quer continuar? [S/N] ')[0].upper()
    if b == 'S':
        continue
    else:
        break