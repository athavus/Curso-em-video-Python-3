cont18 = homem = mulher20 = 0
while True:
    idade = int(input('\033[30mDigite a sua idade:\033[m '))
    sexo = str(input('\033[30mDigite o seu sexo [M/F]:\033[m ')).upper().strip()
    run = str(input('\033[30mVocê gostaria de continuar? [S/N]\033[m ')).upper().strip()
    if idade >= 18:
        cont18 += 1
    if sexo[0] in 'M':
        homem += 1
    if sexo[0] in 'F':
        if idade < 20:
            mulher20 += 1
    if run[0] in 'S':
        print('\033[1;30mOk!\033[m\n')
    else:
        break
print('\033[1;32mFIM DA COMPUTAÇÃO DE DADOS!\033[m')
print(f'\n\033[1;30mTem {cont18} pessoas com mais de 18 anos!\033[m')
print(f'\033[1;30m{homem} homens foram cadastrados!\033[m')
print(f'\033[1;30m{mulher20} mulheres tem menos de 20 anos\033[m')
