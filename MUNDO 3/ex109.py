from utilidadescev import moeda

a = float(input('Digite um valor em R$'))
permais = float(input(f'Digite uma porcentagem para aumentar de {a}: '))
permenos = float(input(f'Digite uma porcentagem para diminuir de {a}: '))
print(f'O dobro de {moeda.moeda(a)} é {moeda.dobro(a, False)}')
print(f'A metade de {moeda.moeda(a)} é {moeda.metade(a, True)}')
print(f'O acréscimo de {permais}% de {a} é igual a {moeda.aumentar(a, permais, True)}')
print(f'O descréscimo de {permenos}% de {a} é igual a {moeda.diminuir(a, permenos, False)}')
