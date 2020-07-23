from time import sleep
from random import choice
class decida_por_mim:
    def __init__(self):
        self.respostas = ['Não faço ideia!',
                     'Sim, Definitivamente.',
                     'Tem certeza que quer fazer isso?',
                     'Talvez sim, talvez não...',
                     'Não, definitivamente não.',
                     'Faça isso e arque com as consequências.',
                     'Não consegui pensar em nada ;c',
                     'Sua vida irá mudar se você fizer isso']


    def Iniciar(self):
        self.FazerPergunta()

    def FazerPergunta(self):
        input('Qual a seu Questionamento ?')
        print('Pensando...')
        sleep(5)
        print(choice(self.respostas))
        fazer_outra_pergunta = input('Gostaria de fazer outra pergunta ? [S/N]').strip()
        if fazer_outra_pergunta in 'Ss':
            self.FazerPergunta()
        elif fazer_outra_pergunta in 'Nn':
            print('Obrigado por Perguntar!!')
        else:
            print('Digite apenas \"S\" ou \"N\"')
            self.FazerPergunta()





decidapormim = decida_por_mim()
decidapormim.Iniciar()
