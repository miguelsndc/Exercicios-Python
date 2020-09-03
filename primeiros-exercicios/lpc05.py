n1 = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
n = n1.count(9)
print(f'Os Números foram {n1}')
print(f'O número 9 aparece {n} vezes.')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3) + 1}ª posição')
else:
    print('O número 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram', end=' ')
for x in n1:
    if x % 2 == 0:
        print(x, end=' ')