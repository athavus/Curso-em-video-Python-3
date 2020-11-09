frase = input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez no caractere {}'.format(frase.find('A')+1))
print('A letra A aparece pela última vez no caractere {}'.format(frase.rfind('A')+1))
