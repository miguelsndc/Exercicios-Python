nome = str(input('Digite seu nome completo:')).strip()
print('Analizando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
sep = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(sep[0], len(sep[0])))

