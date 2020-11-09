from utilidadescev import moeda

a = float(input('Digite um valor em R$'))
permais = float(input(f'Digite uma porcentagem para aumentar de {a}: '))
permenos = float(input(f'Digite uma porcentagem para diminuir de {a}: '))
moeda.resumo(a, permais, permenos)
