hour = input('Digite que horas são: ')

if hour.isnumeric():
    hour = int(hour)
    if hour >=0 and hour <= 11:
        print('Bom dia')
    elif hour <= 17:
        print('Boa Tarde')
    elif hour <= 23:
        print('Boa Noite.')
    else:
        print('Horário Inválido')
else:
    print('Digite um número inteiro.')