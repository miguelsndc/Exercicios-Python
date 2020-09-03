lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    if n % 2 == 1:
        listaimpar.append(n)
    cont = str(input('Quer Continuar ? [S/N] '))
    while cont not in 'SsNn':
        c = str(input('Resposta inválida, Deseja Continuar? ')).strip().lower()
        if c in 'n':
            break
    if cont in 'nN':
        print(f'A lista total é {lista}\nOs valores pares são {listapar}\nOs valores ímpares são {listaimpar}')
        break
