#NOME E PREÇO DE VARIOS PRODUTOS
#PERGUNTA SE VAI CONTINUAR
#TOTAL GASTO / QUANTOS CUSTAM MAIS DE 1000 REAIS QUAL O NOME DO PRODUTO MAIS BARAT0
cont = 0
soma = 0
cont1 = 0
menor = 0
barato = ''
while True:
    print('\033[1;34m======LOJA SUPER BOM PREÇO======\033[m')
    nome = str(input('\033[1;30mNome do Produto: ')).strip()
    preco = int(input('\033[1;30mQual o Valor do produto? R$'))
    cont1 += 1
    continuar = str(input('\033[1;31mQuer Continuar? [S/N]')).upper().strip()
    soma += preco
    while continuar not in 'SN':
        continuar = str(input('\033[1;31mQuer Continuar? [S/N]\033[m')).upper().strip()
    if preco >= 1000:
            cont += 1
    if cont1 == 1 or preco < menor:
        menor = preco
        barato = nome
    if continuar == 'N':
            print(f'\033[1;32mO Total da compra foi {soma}.\033[m')
            print(f'\033[1;33mTemos {cont} produto(s) que custam mais de R$1000.\033[m')
            print(f'\033[1;34mO Produto mais barato foi {barato}, que custa {menor:.2f}\033[m.')
            break

