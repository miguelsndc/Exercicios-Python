lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')

