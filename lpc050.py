from random import randint
n = 0
cont = 0
while True:
    print('Vamos jogar Par ou Ímpar!')
    jogador = int(input('Diga um valor: '))
    comp = randint(0,10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {comp} o total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;34mVocê Venceu!!')
            cont += 1
        else:
            print('\033[1;31mVocê Perdeu!!')
            print(f'Você venceu {cont} vezes')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            cont += 1
            print('\033[1;34mVocê Venceu!!')
        else:
            print('\033[1;31mVocê Perdeu!!')
            cont += 1
            print(f'Você venceu {cont} vezes')
            break

