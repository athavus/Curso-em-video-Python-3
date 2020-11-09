a = float(input('Informe o seu salário: '))
if a > 1250:
    aumento = a * 1.10
else:
    aumento = a * 1.15
print(f'O seu salário era R${a:.2f} \nO seu novo salário com aumento será R${aumento:.2f}')
