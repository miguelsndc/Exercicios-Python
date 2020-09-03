import sys
from random import randint
class chute_do_numero:
    def __init__(self):
        self.valor_maximo = 100
        self.valor_minimo = 0
        self.valor_chute = 0
        self.valor_aleatorio = 0


    def ObterValordoUsuario(self):
        try:
            self.valor_chute = int(input(f'Chute um valor entre {self.valor_minimo} e {self.valor_maximo}: '))
        except ValueError:
            print('Favor digitar apenas números')
            self.ObterValordoUsuario()


    def Gerarvaloraleatorio(self):
        return randint(self.valor_minimo, self.valor_maximo)


    def Iniciar(self):
        self.valor_aleatorio = self.Gerarvaloraleatorio()
        self.ObterValordoUsuario()
        while self.valor_aleatorio != self.valor_chute:
            if self.valor_aleatorio > self.valor_chute:
                print('Digite um valor maior...')
                self.ObterValordoUsuario()
            elif self.valor_aleatorio < self.valor_chute:
                print('Digite um valor menor...')
                self.ObterValordoUsuario()

            else:
                sys.exit()
        print('Você Acertou!!')


auto = chute_do_numero()
auto.Iniciar()

