maior = 0
soma = 0
quant = 0
for c in range(0, 5):
    n = int(input('Digite Um Número: '))
    soma += n
    quant += 1
    med = soma / quant
    if n > maior:
        maior = n
print(f'O maior número é o {maior}, a soma entre todos os números é {soma}. e a média é {med}')