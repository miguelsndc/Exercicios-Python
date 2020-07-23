def LeiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except ValueError:
            print('\033[31mERRO, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mExecução interrompida pelo usuário')
            return 0
        else:
            return n1


def LeiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except ValueError:
            print('\033[31mERRO, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mExecução interrompida pelo usuário')
            return 0
        else:
            return n2

n1 = LeiaInt('Digite um número inteiro: ')
n2 = LeiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1}, o número real digitado foi {n2}')