
from time import sleep
class Carro:
    def __init__(self, marca, potenciadomotor, anodefabricacao):
        self.marca = marca
        self.potenciadomotor = potenciadomotor
        self.anodefabricacao = anodefabricacao


    def darapartida(self):
        for c in range(3, 0, -1):
            print(f'Carro ligando em {c}...')
            sleep(0.5)

    def acelerar(self):
        print('Acelerando...')


    def desligar(self):
        print('desligando..')


carro = Carro('Chevrolet', '600CV', '2018')
carro.darapartida()
carro.acelerar()
carro.desligar()
