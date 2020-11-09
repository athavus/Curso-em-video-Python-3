def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mO Usuário resolveu não digitar esse número\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mO Usuário resolveu não digitar esse número\033[m')
            return 0
        else:
            return num


a = leiaInt('Digite um número inteiro: ')
b = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {a} e o real foi {b}')