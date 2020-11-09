a = str(input('Digite a expressão: '))
total = []
for c in a:
    if c == '(':
        total.append('(')
    elif c == ')':
        if len(total) > 0:
            total.pop()
        else:
            total.append(')')
            break
if len(total) == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
