soma = cont = 0
for c in range(0, 2):
    nota = int(input('Digite as Notas do aluno:'))
    soma += nota
    cont += 1
if soma / cont <= 6.9:
    print(f'A Média Do aluno é {soma / cont}, REPROVADO.')
elif soma / cont >= 7:
    print(f'A Média do Aluno é {soma / cont}, APROVADO')