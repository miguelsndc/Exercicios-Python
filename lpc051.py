# CADASTRADOR DE PESSOAS
idade = 0
cont = 0
cont1 = 0
cont2 = 0
while True:
    print('=====\033[1;33mCADASTRO DE PESSOAS\033[m=====')
    idade = int(input('\033[1;32mIdade: '))
    sexo = str(input('\033[1;34mSexo [M/F]\033[m')).upper().strip()
    continuar = str(input('\033[1;31mQuer Continuar [S/N]\033[m')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).upper().strip()
    if idade < 18:
        cont += 1
    if sexo == 'M':
        cont1 += 1
    if sexo == 'F' and idade < 20:
        cont2 += 1
    if continuar == 'N':
        print(f'\033[1;32mAo todo temos {cont} pessoas com menos de 18 anos.')
        print(f'\033[1;33mTemos {cont1} homens cadastrados')
        print(f'\033[1;34mTemos {cont2} mulheres com menos de 20 anos')
        break


