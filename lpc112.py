from time import sleep


def contagem(inicio, fim, passo):
    print('~' * 40)
    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
        print('~' * 40)
    elif inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')
        print('~' * 40)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez!! ')
ini = int(input('Digite o início: '))
fi = int(input('Digite o fim: '))
pas = int(input('Digite o passo:: '))
if pas == 0:
    pas += 1
contagem(ini, fi, pas)