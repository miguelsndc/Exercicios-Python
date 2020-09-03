#crie uma matrix 3x3 inputa numa lista e msotra no final 9 valores
lista = list()
dado = list()
for m in range(1, 10):
    dado.append(int(input(f'Digite o {m}o Valor: ')))
    lista.append(dado[:])
    dado.clear()
print(f'{lista[0]}{lista[1]}{lista[2]}')
print(f'{lista[3]}{lista[4]}{lista[5]}')
print(f'{lista[6]}{lista[7]}{lista[8]}')
