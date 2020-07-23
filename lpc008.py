#EXERCÍCIO 8
def lin():
    print('='*40)


lin()
print('EXERCÍCIO 8')
lin()
tipomed = str(input('Qual o tipo de média você quer tirar ?'))
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
a = (n1 + n2 + n3) / 3
p = ((n1*5) + (n2*3) + (n3*2)) / 10

if tipomed: 'a'
print('Com as notas de {}, {} e {}, usando a média aritmética, o aluno ficou com a média {:.1f}'.format(n1, n2, n3, a))
if tipomed: p
print('Com as notas de {}, {} e {}, usando a média ponderada, o aluno ficou com a nota de {}'.format(n1, n2, n3, p))

