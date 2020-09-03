n = int(input('Digite uma nota: '))
while True:
    if n < 0 or n > 10:
        n = int(input('\033[1;31mERRO, TENTE NOVAMENTE\n'
                  'Digita uma nota: '))
    else:
        print('\033[1;34mNota válida, Obrigado!')
        break
