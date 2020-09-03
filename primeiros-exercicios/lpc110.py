from time import sleep
from sys import exit
class Televisao:
    def __init__(self):
        numero_do_canal = 0
        volume = 0


    def Iniciar(self):
        print('SIMULADOR DE TELEVISÃO')
        self.tv()

    def tv(self):
        try:
            self.numero_do_canal = int(input('Qual canal deseja assistir ? Temos do canal 1 ao 100! '))
            self.mudarVolume()
        except ValueError:
            print('Por favor digite apenas números.')
            self.tv()
        if self.numero_do_canal < 0 or self.numero_do_canal > 100:
            print('Canal não incluso, Temos apenas do 1 ao 99')
            self.tv()
        else:
            while True:
                vol = 0
                print(f'Excelente escolha!, No momento, assistindo ao canal {self.numero_do_canal} ')
                print('Caso deseje mudar digite o canal desejado, digite v para mudar o volume e -1 para desligar a tv.')
                try:
                    self.numero_do_canal = int(input('-------- '))
                    vol = str(input('-------- ')).strip().lower()
                except ValueError:
                    print('Por favor digite apenas números. ')
                    self.tv()
                if vol == 'v':
                    self.mudarVolume()

                while self.numero_do_canal not in range (0,101):
                    print('Canal não incluso, Temos apenas do 1 ao 100')
                    self.numero_do_canal = int(input('--------'))
                    if self.numero_do_canal == 0:
                        print('desligando...')
                        sleep(3)
                        exit()




    def mudarVolume(self):
        self.volume = int(input('Volume: '))
        if self.volume >= 100:
            print('Volume máximo. ')
            self.volume = 100
        elif self.volume <= 0:
            print('MUDO.')
            self.volume = 0
        else:
            if self.volume > 0 and self.volume < 100:
                print(f'Volume setado em {self.volume}')



tevelisao = Televisao()
tevelisao.Iniciar()


