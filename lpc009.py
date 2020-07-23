#LER UM  NÚMERO EM METROS E MOSTRAR QUANTO ELE VALE EM MILÍMETROS E CENTÍMETROS

n1 = int(input('Digite um número em metros, para saber quanto ele vale em centímetros e milímetros: '))
cent = n1 * 100
mili = n1 * 1000
print('O número {} vale {}, em centímetros e {} em milímetros.'.format(n1, cent, mili))
