#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
##"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"#Mora perto da vítima?"
#"Devia para a vítima?"
#"#Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
lista = list()
n1 = str(input('Telefonou para a vítima? [S/N] ')).strip().lower()
n2 = str(input('Esteve no local do crime? [S/N] ')).strip().lower()
n3 = str(input('Mora perto da vítima? [S/N] ')).strip().lower()
n4 = str(input('A vítima tinha dívidas com você? [S/N] ')).strip().lower()
n5 = str(input('Já trabalhou com a vítima? [S/N] ')).strip().lower()
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)
lista.append(n5)
print(lista)
if lista.count('s') == 0:
    print('Você é inocente')
elif lista.count('s') == 1:
    print('Você é um possível suspeito')
elif lista.count('s') == 2:
    print('Você é suspeito.')
elif 3 <= lista.count('s') <= 4:
    print('Você é cumplice.')
elif lista.count('s') == 5:
    print('Você é o assassino')
print(lista.count('s'))