def lin():
    print('=' * 40)


lin()
print('10 TERMOS DE UMA PA')
lin()
n1 = int(input('\033[1;33mPRIMEIRO TERMO: '))
n2 = int(input('\033[1;33mRAZÃO: '))
d = n1 + (10 - 1) * n2
for c in range(n1, d + n2, n2):
    print(c, end=' ')
