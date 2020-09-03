n = int(input('Digite um valor para saber seu fatorial: '))
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
print(f'O fatorial é {fatorial}')