lista = list()
dadopar = list()
dadoimpar = list()
for n in range(1, 8):
    num = int(input(f'Digite o {n}o Valor: '))
    if n % 2 == 0:
        dadopar.append(n)
    else:
        if n % 2 == 1:
            dadoimpar.append(n)
lista.append(dadopar[:])
dadopar.clear()
lista.append(dadoimpar[:])
dadoimpar.clear()
print(f'Os números pares digitados foram {lista[0]}')
print(f'Os números ímpares digitados foram {lista[1]}')