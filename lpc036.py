import sys
print('Então você deseja financiar uma casa, vamos lá!')
cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
igh = str(input('Se o valor da parcela for \033[1;31mmaior que 30% do seu salário\033[m será negado, ok?'))
if igh == 'ok':
    print('Vamos lá então, Vou lhe fazer algumas perguntas.')
else:
    print('OK, Volte sempre!')
    sys.exit()

valcasa = float(input('Qual o Valor da casa que você deseja financiar?'))
temp = int(input('Em quantas parcelas você pretende pagar?'))
sal = int(input('Qual o Seu salário? '))
persal = sal * (30/100)
valxtemp = valcasa / temp
print('Você terá uma parcela de {}{:.2f}{} divididas em {} vezes'.format(cores['azul'], valxtemp, cores['limpa'], temp))
if persal < valxtemp:
    print('Infelizmente você não tem condições de comprar este imóvel, seu financiamento foi \033[1;31mnegado\033[m')
elif persal >= valxtemp:
    print('Parabéns, você foi \033[1;32maprovado\033[m!!')
    print('Entre em contato com um de nossos corretores para efetuar a compra!!')