
#1 peça as quatro notas de 10 alunos, 
#2 calcule e armazene num vetor a média de cada aluno, 
#3 imprima o número de alunos com média maior ou igual a 7.0.

notas = {}
medias = {}
quantidade_de_estudantes = 10
notas_temporarias = []
# pegando inputs
for i in range(1, quantidade_de_estudantes + 1):
  nome_do_aluno = input('Digite o nome do aluno: ')
  for n in range(1, 5):
    #validando notas
    while True:
      try: 
        nota = float(input(f'Digite a {n} nota: '))
      except:
        print('Digite números.')
        continue
      else:
        if nota < 0 or nota > 10:
          print('Digite notas entre 0 e 10.')
          continue
        else:
          notas_temporarias.append(nota)
          break
  print('-' * 30)
  #armazenando notas
  notas[nome_do_aluno] = notas_temporarias[:]
  notas_temporarias.clear()
#calculando media e aprovando/reprovando
for k, v in notas.items():
  media = sum(v) / 4
  situacao = "aprovado" if media >= 7 else "reprovado" 
  medias[k] = [f"Média : {media} Situação : {situacao}"]
#exibindo
for k, v in medias.items():
  print('-' * 30)
  print(k, v)

    




