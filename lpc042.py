#PREÇO NORMAL E CONDIÇAO DE PAGAMENTO A VISTA  CARTAO E COM JUROS NO CARTAO
import sys
print('''\033[1;30mDIGITE O VALOR DO PRODUTO E SAIBA AS CONDIÇÕES DE PAGAMENTO, ESCOLHA UMA DELAS.\033[M
\033[1;33m[ 1 ] À VISTA\033[m
\033[1;32m[ 2 ] À VISTA NO CARTÃO\033[m
\033[1;34m[ 3 ] EM ATÉ 2X NO CARTÃO\033[m
\033[1;31m[ 4 ] 3X OU MAIS NO CARTÃO\033[m''')
prod = int(input('\033[1;30mDigite o valor do produto: \033[m'))
pag = int(input('\033[1;30mEscolha sua forma de pagamento:\033[m'))
par = int(input('''\033[1;30mEscolha em quantas parcelas você quer dividir o pagamento: (CASO NÃO QUERIA DIVIDIR
O PAGAMENTO, DIGITE 1) - \033[m '''))
if pag == 1 and par == 1:
    print('''\033[1;33mPARA PAGAMENTO À VISTA EM ESPÉCIE, TENS UM DESCONTO DE 10% NO VALOR DO PRODUTO, ASSIM, O VALOR
DO PRODUTO É R${}\033[m'''.format(prod - (prod * 10/100)))
elif pag == 2 and par == 1:
    print('''\033[1;32mPARA PAGAMENTO À VISTA NO CARTÃO, TENS UM DESCONTO DE 5% NO VALOR DO PRODUTO, ASSIM, O VALOR DO
PRODUTO É R${}\033[m'''.format(prod - (prod * 5/100)))
elif pag == 3 and par ==2:
    print('''\033[1;34mPARA PAGAMENTO EM ATÉ 2X NO CARTÃO VOCÊ PAGARÁ O VALOR INTEGRAL DO PRODUTO, COM UMA PARCELA DE
R${}\033[m'''.format(prod - (prod * 50/100)))
elif pag == 4 and par >= 3:
    print('''\033[1;31mPARA PAGAMENTO DE 3X OU MAIS NO CARTÃO, TERÁS UM JUROS DE 20%, COMO ESCOLHESTES PAGAR
EM {} VEZES, FICAS COM UMA PARCELA DE R${}, E NO TOTAL, O VALOR DE R${}.\033[m'''.format(par, (prod * 120/100) / par, (prod * 120/100)))
wish = str(input('\033[1;30mDESEJAS PROSSEGUIR COM A COMPRA DO PRODUTO?\033[m ')).strip().upper()
if wish == 'SIM':
    print('\033[1;30mOK, DESEJAS RECEBER O PRODUTO EM SUA CASA OU RETIRÁ-LO NA LOJA MAIS PRÓXIMA?\033[m ')
else:
    print('\033[1;34mOBRIGADO, VOLTE SEMPRE!')
    sys.exit()
rec = str(input('--- ')).strip().upper()
if rec == 'RECEBER EM CASA':
    print('\033[1;30mENTÃO ME CONFIRME SEUS DADOS, CIDADE, ESTADO CEP E COMPLEMENTO')
elif rec == 'RETIRÁ-LO NA LOJA':
    print('\033[1;30mINDIQUE SUA CIDADE PARA QUE POSSAMOS LOCALIZAR UMA DE NOSSAS LOJAS PARA RETIRADA:\033[m')
    cid = str(input('\033[1;30mCIDADE:\033[m ')).strip().upper()
    if cid in 'RECIFE OLINDA PAULISTA BOA VIAGEM CANDEIAS PIEDADE IPOJUCA':
     print('\033[1;30mOK!, PODES RETIRAR O PRODUTO NA NOSSA LOJA OFICIAL EM RECIFE - RUA DA AURORA 752\033[m')
#ENDEREÇO ALEATORIO!
else:
    print('\033[1;30mNÃO TRABALHAMOS COM SUA REGIÃO, OBRIGADO PELA PREFERÊNCIA!\033[m')
    sys.exit()

st = str(input('\033[1;30mESTADO:\033[m ')).strip().upper()
cep = str(input('\033[1;30mCEP:\033[m    ')).strip().upper()
comp = str(input('\033[1;30mCOMPLEMENTO:\033[m ')).strip().upper()
if st == 'PERNAMBUCO' and cep == '50710310' and comp == 'APARTAMENTO 02':
    print('\033[1;30mOK, O PRODUTO CHEGARÁ ENTRE 5 A 10 DIAS, OBRIGADO PELA PREFERÊNCIA!!\033[m')
    sys.exit()
else:
    print('\033[1;30mNÃO TRABALHAMOS COM SUA LOCALIZAÇÃO, OBRIGADO PELA PREFERÊNCIA!\033[m')
    sys.exit()
#SÓ SEI MEU PROPRIO CEP, ENTÃO VAI ELE MESMO KK
































