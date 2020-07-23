num = input('Digite um número inteiro: ')

if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print('O Número é par')
    else:
        print('O Número é ímpar')
else:
    print('Não foi possível efetuar a operação, Verifique se o número digitado é INTEIRO.')