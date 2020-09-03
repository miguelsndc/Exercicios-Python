#PAIS A 80000 3% DE TAXA DE CRESCIMENTO
#PAIS B 200000HABITANTES TAXA DE CRESCIMENTO 1,5%
a = int(input('Digite a população da cidade A: '))
b = int(input('Digite a população da cidade B: '))
cont = 0
if b > a:
    while b > a:
        a += a * 0.03
        b += b * 0.015
        cont += 1
    print(f'A ultrapassa B em {cont} anos\n'
    f'População A: {a:.2f}\n'
    f'População B: {b:.2f}')
if b < a:
    while b < a:
        a += a * 0.03
        b += b * 0.015
        cont += 1
    print(f'B ultrapassa A em {cont} Anos\n'
    f' População A: {a:.2f}\n'
    f' População B: {b:.2f}')
