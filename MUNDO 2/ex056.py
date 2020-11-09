idadetotal = 0
homem = 0
homemvelho = ''
mulher = 0
mulhermenor = 0
idadehomem = 0
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()
    if sexo == 'm':
        homem += 1
    elif sexo == 'f':
        mulher += 1
    else:
        print('Opção inválida!')
    if sexo == 'f' and idade < 20:
        mulhermenor += 1
    if sexo == 'm' and idade > idadehomem:
        idadehomem = idade
        homemvelho = nome
    idadetotal += idade
media = idadetotal/4
print(f'A média total de idade do grupo é {media}\nO nome do homem mais velho é {homemvelho} \nNeste grupo tem '
      f'{mulhermenor} mulheres com menos de 20 anos.')
