from random import randint
rand = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Foram gerados os números {rand}')
print(f'\nO MAIOR dos números gerados foi {max(rand)}')
print(f'O MENOR dos números gerados foi {min(rand)}')
