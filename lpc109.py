from random import randint
from sys import exit
from time import sleep
class ContaCorrente:
    def __init__(self):
        self.numero_da_conta = 0
        self.nome_do_correntista = ''
        self.saldo = 0
        self.saldo_aleatorio = randint(self.saldo, 9999)


    def saque(self):
        self.numero_da_conta = int(input('Digite o número da conta: '))
        while self.numero_da_conta > 999999:
            print('O número da sua conta não pode ter mais de 6 dígitos.')
            self.saque()
            if self.numero_da_conta < 999999:
                break


        print(f'Você possui um saldo de R${self.saldo_aleatorio}')
        valor_a_ser_sacado = int(input('Qual valor você gostaria de sacar ? '))
        if valor_a_ser_sacado > self.saldo_aleatorio:
            print('Saldo Insuficiente.')
            self.saque()
        elif valor_a_ser_sacado <= self.saldo_aleatorio:
            print('Imprimindo as notas...')
            sleep(3)
            print(f'''Ok!, Você irá sacar R${valor_a_ser_sacado}\nficará com R${self.saldo_aleatorio - valor_a_ser_sacado} na sua conta.''')
        operacao_extra_dentrodosaque = input('Gostaria de fazer alguma outra operação? [Depósito/N] ').strip().upper()
        if operacao_extra_dentrodosaque in 'N':
            print('Obrigado por frequentar nosso banco!!')
            exit()
        elif operacao_extra_dentrodosaque in 'DEPOSITODEPÓSITO':
            try:
                self.nome_do_correntista = input('Digite o nome do Correntista: ')
            except ValueError:
                print('Digite apenas números.')
                self.nome_do_correntista = input('Digite o nome do Correntista: ')

            depositar = input(f'Confirma o depósito em nome do {self.nome_do_correntista}? [S/N]').strip()
            if depositar in 'Ss':
                valor_a_ser_depositado = int(input('Digite o valor a ser depositado: '))
                self.numero_da_conta = int(input('Digite o número da conta: '))
                while self.numero_da_conta > 999999:
                    print('O número da sua conta não pode ter mais de 6 dígitos.')
                    self.saque()
                    if self.numero_da_conta < 999999:
                        break


                print(f'Você Irá depositar o valor de R${valor_a_ser_depositado},'
                      f'ficando com um saldo de R${(self.saldo_aleatorio - valor_a_ser_sacado) + valor_a_ser_depositado}')
                print('Obrigado por frequentar nosso banco!!')
                exit()



    def deposito(self):
        self.numero_da_conta  = int(input('Digite o número da sua conta: '))
        while self.numero_da_conta > 999999:
            print('O número da sua conta não pode ter mais de 6 dígitos.')
            self.deposito()
            if self.numero_da_conta < 999999:
                break


        try:
            self.nome_do_correntista = input('Digite o nome do Correntista: ')
        except ValueError:
            self.deposito()

        depositar = input(f'Confirma o depósito em nome do {self.nome_do_correntista}? [S/N]').strip()

        if depositar in 'sS':
            print(f'Você possui um saldo de R${self.saldo}')
            try:
                 valor_do_deposito = float(input('Qual valor você Gostaria de depositar? '))
            except ValueError:
                valor_do_deposito = float(input('Digite apenas números, Qual valor você gostaria de depositar ? '))
            print(f'Agora você possui um saldo de R${self.saldo + valor_do_deposito}')
            operacao_extra_nodeposito = input('Gostaria de fazer mais alguma operação ? [Saque/N]').strip().upper()
            if operacao_extra_nodeposito == 'N':
                print('Obrigado por frequentar nosso banco!!')
                exit()
            elif operacao_extra_nodeposito == 'SAQUE':
                print('-' * 40)
                print('{:^40}'.format('SAQUE'))
                saque_no_deposito = int(input(f'Você possui um saldo de R${self.saldo + valor_do_deposito}, Qual valor gostaria de sacar?'))
                if (self.saldo + valor_do_deposito) < saque_no_deposito:
                    print('Saldo insuficiente.')
                elif (self.saldo + valor_do_deposito) >= saque_no_deposito:
                    print(f'Você sacou um valor de R${saque_no_deposito}, Ficando no saldo de {(self.saldo + valor_do_deposito) - saque_no_deposito}')
                    print('Imprimindo as notas...')
                    sleep(3)
                    print('Obrigado por frequentar nosso banco!')
                    exit()


    def Iniciar(self):
        print('-=' * 25)
        print('{:^50}'.format('BANCO PD'))
        operacao_do_cliente = input('Qual operação você deseja realizar hoje? [SAQUE/DEPOSITO] ').strip().upper()
        if operacao_do_cliente == 'SAQUE':
            self.saque()
        elif operacao_do_cliente in 'DEPOSITODEPÓSITO':
            self.deposito()
        else:
            print('Obrigado por frequentar nosso banco!!')
            exit()



conta = ContaCorrente()
conta.Iniciar()

