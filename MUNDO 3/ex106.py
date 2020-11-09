def manual():
    """manual

    Está função serve para mostrar o manual de um comando que o usuário quiser,
    sendo então uma central de ajuda para comandos do python.
    """
    while True:
        print('\033[1;32m~' * (len('CENTRAL DE AJUDA PYHELP') + 2))
        print(f'CENTRAL DE AJUDA PYHELP'.center(len('CENTRAL DE AJUDA PYHELP') + 2))
        print('~'* (len('CENTRAL DE AJUDA PYHELP') + 2))
        print('\033[m')
        com = input('\033[35mDigite o comando ou biblioteca que você deseja ver o manual:\033[m ')
        if com == 'fim':
            break
        if len(com) == 0:
            print('\033[1;31mVocê não digitou nenhum comando ou bibliteca!\033[m')      
        else:
            print('\033[37m~' * (len(f'MANUAL DO COMANDO "{com}"') + 2))
            print(f'MANUAL DO COMANDO "{com}"'.center(len(f'MANUAL DO COMANDO "{com}"') + 2))
            print('~'* (len(f'MANUAL DO COMANDO "{com}"') + 2))
            print('\033[1;33m')
            help(com)
            print('\033[m')


manual()
print('\033[1;32mEXECUÇÃO ENCERRADA!\33[m')
