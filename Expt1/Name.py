name = input('Digite seu nome: ')

if len(name) <= 4:
    print('Seu nome é curto')
elif len(name) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é Grande.')