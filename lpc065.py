maior = menor = soma = 0
cont = 0
while True:
    n1 = int(input('Digite um número: '))
    continuar = str(input('Quer Continuar? [S/N]')).strip().upper()
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

    if continuar == 'N':
        print(f'O maior número é o {maior}, o menor é o {menor} e a soma entre eles é {soma}')
        break
