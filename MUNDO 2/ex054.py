from datetime import date
contm = 0
contn = 0
for a in range (0, 7):
    b = int(input(f'Digite o ano de nascimento da {a}°: '))
    if date.today().year - b >= 18:
        contm += 1
    else:
        contn += 1
print(f'{contm} já atingiram a maioridade e {contn} não atingiram a maioridade')
