#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
cont = soma = 0
while True:
    cont += 1
    n = int(input(f'Digite o valor do cd {cont} : (Quando desejar PARAR digite 0). '))
    soma += n
    if n == 0:
        print(f'No total de {cont - 1} CDs, foram gastos no total {soma} reais, e a média de custo de cada cd é {soma / (cont - 1)}')
        break