#TEMPO PARA ALISTAMENTO MILITAR AINDA VAI JÁ VAI OU JÁ PASSOU DE ACORDO COM IDADE
print('Digite sua idade para saber A hora do seu \033[1;34malistamento Militar\033[m!!')
n1 = int(input('Digite sua Idade:'))
if n1 < 18:
    print('\033[1;30mVocê ainda vai se alistar no exército, faltam {}(s) anos\033[m.'.format((18 - n1)))
elif n1 == 18:
    print('\033[1;31mJá está na hora do seu Alistamento, dirija-se a uma unidade do exército para fazê-lo!!\033[m')
elif 18 < n1 < 100:
    print('\033[1;35mJá passou do momento do seu alistamento militar em {} anos\033[m.'.format((n1 - 18)))

