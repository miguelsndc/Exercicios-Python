#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

n = 1
p = 0
i = 0
while n <= 10:
    a = int(input('Digite um número: '))
    n += 1
    if a % 2 == 0:
        p += 1
    elif a % 2 != 0:
        i += 1
print(f'Existem {p} números pares e {i} números ímpares.')
