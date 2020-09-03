#ano bissexto
ano = int(input('Digite um ano qualquer e saiba se ele é bissexto: '))
if ano % 4 == 0:
    print('é um ano bissexto.')
else:
    print('Não é um ano bissexto.')