lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer Continuar? [S/N]')).strip().lower()
    if cont == 'n':
        print(f'Há {len(lista)} Valores nesta lista.')
        lista.sort(reverse= True)
        print(f'{lista}')
        if 5 in lista:
            print('O valor 5 está na lista')
            break
        else:
            print('O valor 5 não está na lista.')
            break