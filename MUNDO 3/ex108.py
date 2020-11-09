from utilidadescev import moeda

a = float(input('Digite um valor em R$'))
permais = float(input(f'Digite uma porcentagem para aumentar de {a}: '))
permenos = float(input(f'Digite uma porcentagem para diminuir de {a}: '))
print(f'O dobro de {moeda.moeda(a)} é {moeda.moeda(moeda.dobro(a))}')
print(f'A metade de {moeda.moeda(a)} é {moeda.moeda(moeda.metade(a))}')
print(f'O acréscimo de {permais}% de {a} é igual a {moeda.moeda(moeda.aumentar(a, permais))}')
print(f'O descréscimo de {permenos}% de {a} é igual a {moeda.moeda(moeda.diminuir(a, permenos))}')