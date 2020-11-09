l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('Estes lados não formam um triângulo!')
else:
    print('Estes lados formam um triângulo!')
