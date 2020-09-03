#A PARA ARITMETICA E P PARA PONDERADA 3 NOTAS - FUNÇÃO - MIGUEL SANTOS NOGUEIRA DA COSTA 1C
def mediarit(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def mediapond(n1, n2, n3):
    return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10

n1 = float(input('Digite a primeira nota : ')
n2 = float(input('Digite a Segunda nota : '))
n3 = float(input('Digite a Terceira nota :'))

medarit = mediarit(n1, n2, n3)
medpond = mediapond(n1, n2, n3)

media = input('Qual tipo de média gostaria de tirar ? [A - Aritmética / P - Ponderada]').strip().lower()
if media == 'a':
    print(f'Com as notas de {n1}, {n2} e {n3} a média foi {medarit}')
              
elif media == 'p':
    print(f'Com as notas de {n1} (peso 5), {n2} (peso 3) e {n3} (peso 2) sua média foi de {medpond}')

else:
    print('Digite um comando válido')