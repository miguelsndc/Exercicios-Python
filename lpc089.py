#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
lista = []
listapar = []
listaimpar = []
for c in range (1, 21):
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    if n % 2 == 1:
        listaimpar.append(n)
print(f'{lista}\n{listapar}\n{listaimpar}')

