#Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros.
#Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
#Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
from random import randint
from time import sleep
from sys import exit
class ContaInvestimento():
    def __init__(self, taxa_juros=0, saldo=0):
        self.taxa_juros = taxa_juros
        self.saldo = saldo

    def linha(self, tam=42):
        return '-' * tam


    def construir_conta(self):
        print(self.linha())
        print('CONTA DE INVESTIMENTO'.center(42))
        print(self.linha())
        self.saldo = randint(0, 10000)
        print(f'Você começa com um saldo de R${self.saldo}')
        print(f'A um juros Inicial desconhecido, o Juros é instável e muda constantemente, fique atento.')
        while True:
            try:
                start = input('Começar ? [S/N]').strip().lower()
            except:
                print('Digite um comando válido.')
                continue
            else:
                if start == 's':
                    for c in range(0, 5):
                        self.adicionarjuros()
                    print(f'Saldo atingido : R${self.saldo:.2f}')
                    while True:
                        restart = input('Gostaria de refazer o Processo ? [S//N]').strip().lower()
                        if restart == 's':
                            for c in range(0, 5):
                                self.adicionarjuros()
                            print(f'Saldo atingido : R${self.saldo:.2f}')
                        elif restart == 'n':
                            print(f'Saldo final : {self.saldo}')
                            exit()
                            break
                        else:
                            print('Digite apenas S ou N!')
                            continue
                elif start == 'n':
                    print('Obrigado por participar.')
                    break
                else:
                    print('Digite apenas S ou N!')
                    continue





    def adicionarjuros(self):
        self.taxa_juros = randint(0, 15)
        print(f'Adicionado juros de {self.taxa_juros}%...')
        resultado = self.saldo * (self.taxa_juros/100)
        self.saldo+=resultado
        sleep(1.5)


investir = ContaInvestimento()
investir.construir_conta()
