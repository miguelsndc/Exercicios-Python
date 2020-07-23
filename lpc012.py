#LEITOR DE LARGURA ALTURA

lar = int(input('Digite a largura:'))
alt = int(input('Digite a altura: '))
area = lar * alt
qtdtin = area / 4

print('com uma area de {} metros quadrados, vão ser necessários {} litros de tinta para pintá-lo'.format(area, qtdtin))