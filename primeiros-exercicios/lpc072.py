menor  = 0
for c in range(0, 3):
    produto = float(input('Digite o preço dos Produtos: '))
    menor = produto
    if produto < menor:
        menor = produto
print(f'Você deve optar pelo produto de {menor}, pois ele é o mais barato.')