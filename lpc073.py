#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
n = int(input('Qual a quantidade de turmas? '))
cont = 0
soma = 0
for i in range(1, n + 1):
    numal = int(input('Digite a quantidade de Alunos de cada turma: '))
    cont += 1
    soma += numal
    result = soma / n
    if numal > 40:
        numal = int(input('ERRO, UMA TURMA NÃO PODE TER MAIS DE 40 ALUNOS. Qual a quantidade de Alunos de cada turma? '))
print(f"Para as {cont} turmas, A média de alunos em cada turma é: {result}")