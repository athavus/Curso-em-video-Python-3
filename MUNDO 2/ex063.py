print('-' * 22)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 22)
a = int(input('Digite quantos termos você quer mostrar: '))
b = 1
fn = 0
fb = 1
print(f'{fn} -> {fb}', end='')
while a >= b:
    fc = fn + fb
    print(f' -> {fc}', end='')
    fn = fb
    fb = fc
    b += 1
print('\nFIM!')
