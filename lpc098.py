
while True:
    print('-' * 40)
    n = int(input('Você Vendeu: '))
    b = (n * (9/100)) + 200
    a = list()
    a.append([n, b])
    print(f'Vendendo R${a[0][0]}\nVocê tem uma comissão de R${a[0][1]}.')
    if 200 <= a[0][1] <= 299:
        print('Você Está na 6ª Divisão')
    if 300 <= a[0][1] <= 399:
        print('Você Está na 5ª Divisão')
    if 400 <= a[0][1] <= 499:
        print('Você Está na 4ª Divisão')
    if 500 <= a[0][1] <= 599:
        print('Você Está na 3ª Divisão')
    if 600 <= a[0][1] <= 699:
        print('Você Está na 2ª Divisão')
    if 700 <= a[0][1] <= 799:
        print('Você Está na 1ª Divisão')
    if a[0][1] > 800:
        print('Você está na divisão 0, Obrigado!!')
    a.clear()
    d = str(input('Próximo... [OK/N]')).strip().upper()
    if d == 'N':
        break
print('<<< Obrigado por participarem, Sejam Bem vindos!!')
