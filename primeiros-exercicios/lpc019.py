#ANGULO QUALQUER SENO COSSENO TANGENTE
import math
n1 = int(input('Digite o Valor do ângulo: '))
sen = math.sin(n1)
cos = math.cos(n1)
tang = math.tan(n1)
print('Para o ângulo {:.2f}, o valor do seno é igual a {:.2f}, o do cosseno é {:.2f} e da tangente é igual a {}'.format(n1, sen, cos, tang))
