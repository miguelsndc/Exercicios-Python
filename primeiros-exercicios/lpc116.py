from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1' : randint(1, 6),
             'Jogador2' : randint(1, 6),
             'Jogador3' : randint(1, 6),
             'Jogador4' : randint(1, 6)
             }
ranking = []
for k, v in jogadores.items():
    print(F' O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('{:^40}'.format('RANKING'))
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
