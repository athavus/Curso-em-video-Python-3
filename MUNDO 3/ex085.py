todos = [[], []]

for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
todos[0].sort()
todos[1].sort()
print(f'\nOs valores lidos foram {todos}')
print(f'Os valores pares lidos foram {todos[0]}')
print(f'Os valores ímpares lidos foram {todos[1]}')
