#A PARA ARITMETICA E P PARA PONDERADA 3 NOTAS - FUNÇÃO - MIGUEL SANTOS NOGUEIRA DA COSTA 1C
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
med = str(input('Digite A para Tirar média aritmética e P para média ponderada: ')).upper().strip()
med4p: float = ((n1 * 5) + (n2 * 3) + (n2 * 2)) / 10
med4a: float = (n1 + n2 + n3) / 3

def aritmed():
    print('Com a média aritmética, seu aluno obteve uma média final de {:.1f}'.format(med4a))


def pondmed():
    print('Com a média ponderada, seu aluno obteve uma média final de {:.1f}'.format(med4p))


if med == 'A':
    aritmed()
else:
    pondmed()
if med4a >= 6:
    print('Está APROVADO.')
else:
    print('Está REPROVADO.')
