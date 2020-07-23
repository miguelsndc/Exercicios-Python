nome = str(input('\033[1;30mQual o seu nome?\033[m')).strip()
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
if nome in 'Miguel':
    print('Tenha um bom dia {}{}{}'.format(cores['azul'], nome, cores['limpa']))

if nome == 'Miguel':
    print('Que nome bonito você tem!!')
elif nome == 'Pedro' or nome == 'Cezar' or nome == 'Ana Paula':
    print('Um dos meus Familiares tem esse nome!!, {}{}{}!'.format(cores['verde'], nome, cores['limpa']))
elif nome in 'Gustavo Felipe Eduarda Cloves':
    print('\033[1;33mQue nome tão bonito quanto Miguel Você tem!,\033[m {}{}{}.'.format(cores['azul'], nome, cores['limpa']))
    print('\033[1;32mTenha um ótimo dia!\033[m')
else:
    print('Que nome não tão bonito quanto Miguel você tem {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
