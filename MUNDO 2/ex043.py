a = float(input('Digite o seu peso: '))
b = float(input('Digite a sua altura: '))
imc = a / (b ** 2)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f} e você está no estado: \n\033[1;31mABAIXO DO PESO\033[m!')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.1f} e você está no estado: \n\033[1;32mPESO IDEAL\033[m!')
elif 25 <= imc < 30:
    print(f'Seu imc é {imc:.1f} e você está no estado: \n\033[1;30mSOBREPESO\033[m!')
elif 30 <= imc < 40:
    print(f'Seu imc é {imc:.1f} e você está no estado: \n\033[1;33mOBESIDADE\033[m!')
elif imc > 40:
    print(f'Seu imc é {imc:.1f} e você está no estado: \n\033[4;31OBESIDADE MÓRBIDA\033[m!')
