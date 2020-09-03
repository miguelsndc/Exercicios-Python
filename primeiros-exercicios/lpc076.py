
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
...
#50 - R$ 99.50

cont = 0
cont1 = 0
cont2 = 0
for i in range(1, 51):
    cont2 += 2
    cont += 1
    cont1 += 0.01
    print(f' #{cont} - R${(cont2 - cont1):.2f}')
