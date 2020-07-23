def lin():
    print('='*40)


lin()
print('Curso em vídeo Operadores aritméticos')
lin()
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
d = n1 / n2
m = n1 * n2
e = n1**n2
di = n1 // n2
print('A some destes valores vale {},\n divisão vale {:.2f},\n a multiplicação é igual a {} \n'.format(s, d, m), end= '>>>')
print('A potência destes valores vale {},\n e a divisão inteira vale {}'.format(e, di))
lin()
print('                  FIM')
lin()
