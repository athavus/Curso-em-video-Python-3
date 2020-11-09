from utilidadescev import moeda, dado

a = dado.leiadinheiro('Digite o preço: R$')
permais = float(input(f'Digite uma porcentagem para aumentar de {a}: '))
permenos = float(input(f'Digite uma porcentagem para diminuir de {a}: '))
moeda.resumo(a, permais, permenos)
