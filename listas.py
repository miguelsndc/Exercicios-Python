import random
lista_de_palavras = ('gasolina',
            'guloso',
            'Luisa',
            'musica',
            'parafuso',
            'pesado',
            'raposa',
            'resumo',)
secreto = random.choice(lista_de_palavras)
digitadas = []
chances = 5

while True:
    if chances == 0:
        print(F'Você não tem mais chances...')
        print('Você perdeu')
        print(f'A palavra era: {secreto.upper()} ')
        break
    else:
        print(f'Chances Restantes : {chances}')
    letra = input('Digite uma letra: ').lower().strip()

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'A letra {letra} NÃO existe na palavra secreta')
        chances -= 1
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario.count('*') == 0:
        print(F'PARABÉNS, A PALAVRA É \033[31m{secreto.upper()}\033[m')
        break

