nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    print('\033[1;31mREPROVADO!')
elif media >= 5 and media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO!')
elif media >= 7:
    print('\033[1;32mAPROVADO!')
