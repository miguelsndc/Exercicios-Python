secreto = 'purfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(F'\nA letra {letra} existe na palavra secreta.')
    else:
        print(f'\nA letra {letra} NÃO existe na palavra secreta.')
        digitadas.pop()
        
    for k in digitadas:
        print(k, end='-')
        