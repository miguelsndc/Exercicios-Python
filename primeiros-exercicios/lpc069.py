letra = input('Digite seu Gênero: [M/F] ').strip().upper()
while letra not in 'MF':
    letra = input('Dados Inválidos. Digite seu Gênero: [M/F]').strip().upper()
if letra == 'M':
    print('Gênero Masculino')
elif letra == 'F':
    print('Gênero Feminino')
