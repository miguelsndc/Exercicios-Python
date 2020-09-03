print('-=' * 20)
print('{:^40}'.format('TABUADA'))
print('-=' * 20)
n2 = int(input('Tabuada de: '))
n = int(input('Começar por: '))
n1 = int(input('Terminar em: '))
for c in range(n, n1 + 1):
    if n >= n1:
        print('Valores inválidos, tente novamente.')
        break
    else:
        print(f'{n2} x {c} = {n2 * c}')