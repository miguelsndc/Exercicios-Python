def conectarwifi():
    for c in range(3, 0, -1):
        print(f'Conectando ao wifi... Tempo restante: {c}')
    print('Conectado ao wifi')


def senhawifi():
    senha=  int(input('Digite sua senha: '))
    while senha != 123456:
        senha = int(input('Senha Incorreta. Digite sua senha: '))
        if senha == 123456:
            print('Senha correta. Conectando...')

 