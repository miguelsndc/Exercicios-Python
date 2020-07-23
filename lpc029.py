#par ou impar
n1 = int(input('Digite um número: '))
cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;;34m'}
if n1 % 2 == 0:
    print('O número {}{}{} é \033[1;34mpar\033[m'.format(cores['amarelo'], n1, cores['limpa']))
else:
    print('O número {}{}{} é \033[1;31mímpar\033[m'.format(cores['azul'], n1, cores['limpa']))
