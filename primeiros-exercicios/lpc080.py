#Os números primos possuem várias aplicações dentro da Computação,
#por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
print('DIGITE 0 PARA FINALIZAR A OPERAÇÃO')
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        cont+=1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end= ' ')
if cont <= 2:
    print('ESTE NÚMERO É PRIMO')
else:
    print('ESTE NÚMERO NÃO É PRIMO')
