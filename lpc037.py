num = int(input('Digite um número \033[1;30mINTEIRO:\033[m '))
print('''\033[1;30mEscolha uma das bases para conversão:\033[m 
[ 1 ] \033[1;30mConversão para Binário\033[m
[ 2 ] \033[1;33mConversão para Octal\033[m
[ 3 ] \033[1;34mConversão para Hexadecimal\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('\033[1;30m{}\033[m Convertido para \033[1;30mBÍNÁRIO\033[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\033[1;33m{}\033[m Convertido para \033[1;33mOCTAL\033[m é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\033[1;34m{}\033[m Convertido para \033[1;34mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
