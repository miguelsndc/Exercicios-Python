##limite de velocidade acima de 80 multa 7 reais por km aci
vel = int(input('O veículo estava a quanto Km/H ?'))
cores = {'limpa': '\033[m',
         'red': '\033[1;31m'}
mul = (vel - 80) * 7
if vel > 80:
    print('Tu tá acima da velocidade permitida, infelizmente vou ter que aplicar uma multa de {}{}{} reais'.format(cores['red'], mul, cores['limpa']))
else:
    print('Tá \033[1;34mlimpo\033[m, pode seguir cidadão.')

