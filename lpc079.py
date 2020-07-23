#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem com
# o a média das temperaturas.
cont = menor = maior = soma = 0

while True:
    n = float(input('Informe a Temperatura: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cn = str(input('Quer Continuar? [S/N]')).strip().lower()
    if cn == 'n':
        print(F'FORAM INFORMADAS {cont} TEMPERATURAS, A MAIOR É A {maior}ºC, A MENOR É A {menor}ºC, A MÉDIA É {soma / cont}ºC')
        break