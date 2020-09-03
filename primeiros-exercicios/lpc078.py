
print('-=' * 20)
print('{:^40}'.format('\033[32mPRODUTO ALEATÓRIO QUALQUER.CIA\033[m'))
print('-=' * 20)
cont = soma = 0
print('DIGITE \033[1;30m0\033[m PARA FINALIZAR A OPERAÇÃO')
while True:
    cont += 1
    n = float(input(f'Produto {cont}: R$ '))
    soma += n
    if n == 0:
        print(f'TOTAL: R$ {soma}')
        n1 = int(input('Dinheiro a ser recebido: '))
        if n1 - soma >= 0:
            print(f'TROCO: {(n1 - soma):.2f}\n'
                  f'OBRIGADO POR FREQUENTAR AS PRODUTO ALEATÓRIO QUALQUER.CIA!!')
            break
        else:
            n2 = str(input('\033[31mDinheiro insuficiente,\033[m Gostaria de adicionar mais dinheiro ou cancelar a compra? [A/C]')).strip().upper()
            if n2 == 'A':
                print('OK, DIGITE O VALOR A SER ADICIONADO: ')
                n3 = float(input('--------'))
                if (n3 + n1) - soma < 0:
                    print('\033[31mDINHEIRO AINDA INSUFICIENTE\033[m, NÃO É POSSÍVEL REALIZAR MAIS ADIÇÕES, REFAÇA O PROCESSO.')
                    break
                else:
                    print(F'TROCO DE R${(n3 + n1) - soma}, OBRIGADO PELA PREFERÊNCIA !!!')
                    break
            else:
                print('\033[31mOPERAÇÃO CANCELADA.\033[m')
                break
