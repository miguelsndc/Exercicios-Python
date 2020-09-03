def lin():
    print('\033[32m-=' * 40)


lin()
print('{:^80}'.format('\033[1;36mVALIDADOR DE DADOS\033[m'))
lin()

nome = str(input('\033[1;34mDigite seu nome: ')).strip()
while len(nome) < 3:
    nome = str(input('\033[1;31mDados Inválidos.\033[m \033[1;30mDigite seu nome:\033[m ')).strip()
idade = int(input('\033[1;30mDigite sua idade:\033[m '))
while idade < 0 or idade > 110:
    idade = int(input('\033[1;31mDados Inválidos.\033[m \033[1;30mDigite sua idade:\033[m '))
sexo = str(input('\033[1;36mDigite seu sexo: [M/F]'))
while sexo not in 'MmFf':
    sexo = str(input('\033[1;31mDados Inválidos.\033[m \033[1;30mDigite seu sexo:\033[m [M/F]'))
salario = int(input('\033[1;33mDigite seu salário: '))
while salario < 0:
    salario = int(input('\033[1;31mDados Inválidos.\033[m \033[1;30mDigite seu salário:\033[m '))
estadocivil = str(input('\033[1;30mDigite seu Estado Civil: '))
while estadocivil not in 'SsCcDdVv':
    estadocivil = str(input('\033[1;31mDados Inválidos.\033[m \033[1;30mDigite seu Estado Civil: [S/C/V/D]\033[m '))
print(f'''\033[1;30mSeu nome é\033[m \033[1;34m{nome}\033[m\n\033[1;30mVocê tem\033[m \033[1;30m{idade}\033[m \033[1;30manos\033[m
\033[1;30mRecebe R$\033[m\033[1;33m{salario}\033[m \033[1;30mpor mês.\033[m''')
if sexo in 'Mm':
    print('\033[1;36mVocê é do sexo Masculino.')
else:
    print('\033[1;36mVocê é do sexo Feminino.')
if estadocivil in 'Ss':
    print('\033[1;30mVocê é\033[m \033[1;32mSolteiro(a).')
elif estadocivil in 'Cc':
    print('\033[1;30mVocê é \033[1;31mCasado(a)')
elif estadocivil in 'Dd':
    print('\033[1;30mVocê é \033[1;34mDivorciado(a)')
else:
    print('\033[1;30mVocê é \033[1;37mViúvo(a)')