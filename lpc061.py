cont = 1
n = int(input('Você deseja ver a tabuada de qual número? '))
print(f'Tabuada de {n}:')
for c in range(1, 11):
    print(f'{n} X {c} = {n * c}')

