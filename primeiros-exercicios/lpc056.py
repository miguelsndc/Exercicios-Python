nome = str(input('Digite seu nome: '))
senha = str(input('Digite sua senha: '))
while nome == senha:
    print('\033[1;31nERRO... A SENHA DO USUÁRIO NÃO PODE SER IGUAL AO NOME. TENTE NOVAMENTE\033[m')
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: '))
    if nome != senha:
        print('SEJA BEM VINDO!')
        break