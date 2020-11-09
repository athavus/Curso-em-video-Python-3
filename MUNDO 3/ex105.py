def notas(* num, sit=False):
    """notas

    Parâmetros:
        num (array): É a lista de notas que será recebido para calcular os dados do aluno
        sit (bool, optional): É o parâmetro para mostrar ou não a situação do aluno. Defaults to False.

    Returns:
        dados (dict): Dicionário com as informações do aluno
    """    
    dados = {'Quantidade de notas': len(num), 'Maior nota': max(num),
             'Menor nota': min(num), 'Média das notas': (sum(num) / len(num))}
    if dados['Média das notas'] >= 7 and sit == True:
        dados['SITUAÇÃO'] = 'Aprovado'
    elif 5 <= dados['Média das notas'] < 7 and sit == True:
        dados['SITUAÇÃO'] = 'Razoável'
    elif dados['Média das notas'] < 5 and sit == True:
        dados['SITUAÇÃO'] = 'Ruim'
    return dados


a = notas(5, 6, 7.5, 8)
print(a)
