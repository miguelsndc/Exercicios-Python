#sorteio alunos
import random
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno:  '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno:   '))
list = [al1, al2, al3, al4]
Esql = random.shuffle(list)
print('A ordem de apresentação será')
print(list)
