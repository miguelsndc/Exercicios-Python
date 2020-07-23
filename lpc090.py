gaelra = list()
dados = list()
tomai = tomen = 0
for c in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    gaelra.append(dados[:])
    dados.clear()
print(gaelra)
for p in gaelra:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tomai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tomen += 1
print(f'Temos {tomai} pessoas maiores de idade.\nTemos {tomen} pessoas menores de idade.')
