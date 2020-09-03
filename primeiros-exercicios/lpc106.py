#gerador de bolas aleatórias
from random import choice
from time import sleep
class bola:
    def __init__(self):
        self.cor = ['Azul', 'Amarela', 'Vermelha', 'Roxo', 'Verde']
        self.material_da_bola = ('Plástico', 'Couro Sintético')

    def Trocacor(self):
        print(f'A sua bola será da cor {choice(self.cor)}.')
        print(f'O material da sua bola será {choice(self.material_da_bola)}')
        trocar_bola = input('Gostaria de tentar uma nova combinação de bola ?').strip()
        if trocar_bola in 'Ss':
            print('Gerando uma nova bola...')
            sleep(2)
            self.Trocacor()
        elif trocar_bola in 'Nn':
            print('Ok!! Bola definida.')


    def Iniciar(self):
        self.Trocacor()


bolas = bola()
bolas.Iniciar()
