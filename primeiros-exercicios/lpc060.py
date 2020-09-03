n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = 0
while n2 < n1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
else:
    for i in range(n1, n2, 1):
      print(i, end=' ')
      s += i
print(f'A soma dos números entre {n1} e {n2} é {s}')
