lista = list()
listaaux = list()
for c in range(1, 6):
    listaaux.append(float(input('Altura: ')))
    listaaux.append(float(input('Peso: ')))
    lista.append(listaaux[:])
    listaaux.clear()
lista.sort(reverse= True)
for p in lista:
    print(f'As Alturas e Peso, Respectivamente: : {p}')