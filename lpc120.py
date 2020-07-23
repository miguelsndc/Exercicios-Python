#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
##Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


def alcool(litro):
    if litro <= 20:
        return (litro * 1.90) - ((litro * (2.50)) * (3 / 100))
    elif litro > 20:
        return (litro * 1.90) - ((litro * (2.50)) * (5 / 100))


def gasolina(litro):
    if litro <= 20:
        return (litro * 2.50) - ((litro * (2.50)) * (4 / 100))
    elif litro > 20:
        return (litro * 2.50) - ((litro * (2.50)) * (6 / 100))


def iniciar():
    print('-' * 35)
    print('{:^35}'.format('POSTO DO BETÃO'))
    print('Alcoól - R$1,90 L\nGasolinha R$2,50 L')
    b = input('Qual o tipo de combustível :[A/G] ').strip()
    while b not in 'AaGg':
        print('Só temos Alcoól e Gasolina... Escolha [A/G]')
        b = input('Qual o tipo de combustível :[A/G] ').strip()
    if b in 'Aa':
        a = float(input('Total de Litros em Alcool: '))
        litros = alcool(a)
        print(f'Um total de R${litros:.2f}')
    elif b in 'Gg':
        a = float(input('Total de Litros em Gasolina: '))
        litros = alcool(a)
        print(f'Total de R${litros:.2f}')

iniciar()
