n1 = float(input('Digite sua prmeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
m = (n1 + n2) / 2
print('Sua média foi igual a {:.1f}'.format(m))
if m >= 6.0 < 10:
    print('Você está aprovado!')
else:
    print('Você Está reprovado!')