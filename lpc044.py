ps = ('Corinthians', 'Grêmio', 'Cruzeiro', 'Santos', 'São Paulo',
      'Flamengo', 'Atlético-Mineiro', 'Palmeiras', 'Internacional',
      'Fluminense', 'Vasco da Gama', 'Atlético-PR', 'Botafogo',
      'Coritiba', 'Goiàs', 'Figueirense', 'Ponte Preta', 'Bahia',
      'Sport', 'Vitória', 'Chapecoense')
print(f'\033[1;32mOs times são: {ps}\033[m')
print(f'\033[1;33mOs 5 Primeiros Colocados são {ps[0:5]}.\033[m')
print(f'\033[1;31mOs 4 últimos colocados são {ps[-4:]}.\033[m')
print(f'\033[1;34mOs times, Organizados em ordem álfabética são: {sorted(ps)}\033[m')


