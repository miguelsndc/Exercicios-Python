from random import randint
from time import sleep

def sorteio(list):
    print('Sorteando...')
    print('Os valores sorteados foram: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        list.append(n)
        print(f'{n}', end= ' ', flush=True)
        sleep(0.5)
    print('\n')

def soma(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares sorteados é igual a {soma}')



numeros = list()
sorteio(numeros)
soma(numeros)
