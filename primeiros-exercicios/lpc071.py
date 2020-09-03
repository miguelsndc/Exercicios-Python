maior = menor = 0
for c in range(0, 3):
    m = int(input('Digite um número: '))
    if m > maior:
        maior = m
        menor = m
    if m < menor:
        menor = m
print(f'O Maior número é o {maior}, e o menor é o {menor}.')
