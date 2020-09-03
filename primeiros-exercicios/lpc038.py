#VALOR MAIOR MENOR E IGUAL COMPARAÇÃO DE VALORES
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número'))
if n1 > n2:
    print('O número \033[1;31m{}\033[m é \033[1;36mMAIOR\033[m.'.format(n1))
elif n1 < n2:
    print('O número \033[1;31m{}\033[m é \033[1;36mMAIOR\033[m.'.format(n2))
else:
    print('Não existe valor maior, \033[1;35mOS DOIS SÃO IGUAIS.\033[m')
