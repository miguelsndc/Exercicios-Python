#preço da viagem
dist = int(input('Qual a distância percorrida na viagem? '))
if dist <= 200:
    print('Foi uma viagem de {}km, vou cobrar {} por ela.'.format(dist, (dist / 2)))
if dist > 200:
    print('Foi uma viagem longa, de {}km, foi cobrar {:.2f} por ela.'.format(dist, (dist * 0.45)))

