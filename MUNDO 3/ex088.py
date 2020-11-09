from random import randint
from time import sleep
palpites = []
num = int(input('Digite quantos palpites você quer: '))
print()
a = 1
while num > 0:
    sleep(0.5)
    for c in range(0, 6):
        palpites.append(randint(1, 60))
    print(f'PALPITE {a}: {palpites}')
    palpites.clear()
    num -= 1
    a += 1
