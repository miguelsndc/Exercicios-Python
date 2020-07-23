from random import randint
from time import sleep
from sys import exit

class Simulador_de_Dados():
    def __init__(self, vezes_a_sortear=0):
        self.vezes_a_sortear = vezes_a_sortear
        self.total_de_valores = []

    def linha(self, tam=42):
        return '-' * tam

    def main(self):
        print(self.linha())
        print('SIMULADOR DE ROLAR OS DADOS'.center(42))
        print(self.linha())
        valores_sorteados = []
        while True:
            try:
                self.vezes_a_sortear = int(input('Digite Quantos Valores Sortear : '))
            except ValueError:
                print('Digite um Valor válido !! ')
                continue
            else:
                for valor in range(0, self.vezes_a_sortear):
                    sorteados = randint(1, 6)
                    print(sorteados, end=' ')
                    valores_sorteados.append(sorteados)
                    self.total_de_valores.append(sorteados)
                    sleep(0.8)
                print()
                print(F'Os valores sorteados foram {valores_sorteados}')
                while True:
                    try:
                        repetir = input('Repetir o Processo : [S/N]').strip().lower()
                    except ValueError:
                        print('Digite apenas S ou N.')
                        continue
                    else:
                        if repetir == 's':
                            self.main()
                        elif repetir == 'n':
                            print(self.linha())
                            print('\033[91mFIM DO SORTEIO\033[m'.center(42))
                            print(f'Total de valores sorteados até o encerramento : {self.total_de_valores}')
                            exit()
                        else:
                            print('Digite apenas S ou N. ')
                            continue

simulacao = Simulador_de_Dados()
simulacao.main()
