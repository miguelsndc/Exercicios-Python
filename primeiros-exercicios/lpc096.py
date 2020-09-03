from time import sleep
p = list()
cont = 0
while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    continuar = str(input('Quer Continuar ?? [S/N]'))
    p.append([n, [n1, n2], med])
    cont += 1
    while continuar not in 'SsNn':
        continuar = str(input('Resposta Inválida. Digite apenas S/N, Quer continuar ?  [S/N]'))
    if continuar in 'Nn':
        break
print('-' * 26)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 26)
for i, a in enumerate(p):
    print(f'{i:<4}{a[0]:<10}{a[2]:>10}')
    sleep(0.5)
while True:
    print('-' * 35)
    aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(p) - 1:
            print(f'Notas de {p[aluno][0]} são {p[aluno][1]}')
print('<<< VOLTE SEMPRE >>>')

