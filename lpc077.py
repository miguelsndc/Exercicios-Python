#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
...
#50 - R$ 9.00
cont = 0
for i in range(1, 51):
    cont += 0.18
    print(f'#{i} - R$ {cont:.2f}')