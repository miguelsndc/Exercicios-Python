lista = []
for c in range(1, 5):
    lista.append(float(input(f'Digite a {c}ª nota: ')))

lista.sort()
print(f'As notas foram {lista}')
print(f'A média é {sum(lista) / len(lista)}!')