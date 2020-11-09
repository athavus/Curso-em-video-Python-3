l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('Estes lados não formam um triângulo!')
else:
    print('Estes lados formam um triângulo!')
    if l1 == l2 and l1 == l2:
        print('\033[31mTRIÂNGULO EQUILÁTERO!\033[m')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('\033[32mTRIÂNGULO ESCALENO!\033[m')
    else:
        print('\033[34mTRIÂNGULO ISÓSCELES!\033[m')
