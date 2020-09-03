frase = str(input('Digite uma frase:')).strip().upper()
n1 = frase.count('A')
n2 = frase.find('A')+1
n3 = frase.rfind('A')+1
print('Nesta frase a letra a aparece {} vezes'.format(n1))
print('A primeira vez que a letra a apareceu nesta frase foi na posição {}'.format(n2))
print('A última vez que a letra a aparece na frase é na posição {}'.format(n3))
