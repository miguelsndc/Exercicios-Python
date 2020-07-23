from time import sleep
from random import choice
class dado:
    def __init__(self):
        self.numeros_do_dado = (1, 2, 3, 4, 5, 6)


    def Iniciar(self):
        self.Rolarodado()


    def Rolarodado(self):
        print('Rolando os dados...')
        sleep(1)
        print(choice(self.numeros_do_dado))
        rolar_novamente = input('Gostaria de rolar o dado novamente? [S/N]').strip()
        if rolar_novamente in 'Ss':
            self.Rolarodado()
        elif rolar_novamente in 'nN':
            for c in range(3, 0 , -1):
                print(f'Encerrando em {c}...')
                sleep(1)
            print('Encerrado.')
        else:
            print('Por favor digite apenas \'s\' ou \'n\'')
            self.Rolarodado()



rolarosdados = dado()
rolarosdados.Iniciar()
