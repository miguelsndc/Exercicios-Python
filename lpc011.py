#CONVERSOR DE REAIS PARA DÓLARES


def lin():
    print('=' * 40)


lin()
print('CONVERSOR REAL PARA DÓLAR')
lin()

n1 =int(input('Digite um valor em reais aqui e saiba o quanto ele vale em dólar: '))
n2 = n1 / 5.81
print('{} reais valem {:.2f} dólares'.format(n1, n2))

lin()
print('    FIM DA CONVERSÃO')
lin()
