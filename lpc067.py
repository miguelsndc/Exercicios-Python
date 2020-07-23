#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
jose = 0
lula = 0
bolso = 0
num = int(input('\033[30mQual o total de Eleitores:\033[m '))
for c in range(0, num, 1):
    print('\033[1;30m-=\033[m' * 20)
    print('{:^50}'.format('\033[1;33mELEIÇÕES 2022\033[m'))
    print('\033[1;30m-=\033[m' * 20)
    voto = int(input('\033[31mVOTE [ 1 ] PARA LULA\033[m\n'
                     '\033[34mVOTE [ 2 ] PARA JOSÉ\033[m\n'
                     '\033[33mVOTE [ 3 ] PARA BOLSONARO\033[m\n'
                     '--------------- '))
    if voto == 1:
        print('\033[31mObrigado por seu voto!!\033[m')
        lula += 1
    elif voto == 2:
        print('\033[34mObrigado por seu voto!!\033[m')
        jose += 1
    else:
        print('\033[33mObrigado por seu voto!!\033[m')
        bolso += 1

if bolso > lula and jose:
    print(f'\033[33mO vencedor das Eleições foi Bolsonaro, Com {bolso} Votos. ')
if lula > jose and bolso:
    print(f'\033[31mO vencedor das Eleições foi Lula, com {lula} Votos. ')
if jose > lula and bolso:
    print(f'\033[34mO vencedor das Eleições foi José, com {jose} Votos. ')
if bolso == lula == jose:
    print('\033[31mELEIÇÕES EMPATADAS, REFAÇA O PROCESSO, NÃO SOU TÃO BOM PARA FAZER UM SEGUNDO TURNO, OBRIGADO.')