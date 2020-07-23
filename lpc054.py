import random
pe = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
print('Os valores sorteados foram:', end=' ')
for n in pe:
    print(f'{n}', end=' ')

print(f'\nO maior valor é {max(pe)}')
print(f'O menor valor é {min(pe)}')
