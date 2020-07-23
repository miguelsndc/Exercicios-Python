cont = 0
soma = 0
while True:
    n = int(input('Digite as notas: 0/10 '))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if n < 0 or n > 10:
        n = int(input('Nota inválida. Digite as notas: '))
    cont += 1
    soma += n
    med = soma / cont
    if continuar == 'N':
         print(f'As média das {cont} notas inseridas é {med:.2f}')
         break