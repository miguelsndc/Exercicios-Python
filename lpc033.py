# aumento de salario
sal = int(input('Qual o seu salário? '))
sal1 = (sal * (10/100))
sal2 = (sal * (15/100))
if sal >= 1250:
    print('Você terá um aumento de 10%, ficando com um salário total de {}.'.format((sal + sal1)))
else:
    print('Você terá um aumento de 15%, ficando com um salário total de {}.'.format((sal + sal2)))
