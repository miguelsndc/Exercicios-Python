while True:
    string_digitada = str(input('Digite uma palavra'))
    if string_digitada.lower().strip() == 'sair':
        print('fim')
        break
    if len(string_digitada) < 2:
        print('String Muito pequena')
        continue
    print('Tente digitar \sair')
