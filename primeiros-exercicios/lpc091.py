pessoas = list()
dado = list()
totpe = maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            dado[1] = menor
    totpe += 1
    n = str(input('Quer Continuar ? [S/N]')).strip()
    pessoas.append(dado[:])
    dado.clear()
    if n in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {totpe} Pessoas')
print(f'O maior peso foi de {maior}Kg, Que é o peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}\n', end='')
print(f'O menor peso foi o de {menor}Kg, que é o peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')
