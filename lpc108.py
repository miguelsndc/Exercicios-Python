from math import hypot, ceil
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {}'.format(ceil(hip)))
