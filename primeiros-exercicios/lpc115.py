def voto(ano_de_nascimento):
    idade = 2020 - ano_de_nascimento
    if 18 >= idade < 65:
        print(f'Com {idade} anos:', end= ' ')
        return 'VOTO OBRIGATÓRIO'
    elif idade < 18:
        print(f'Com {idade} anos:', end=' ')
        return 'NÃO VOTA'
    elif idade >= 65:
        print(f'Com {idade} anos:', end=' ')
        return 'VOTO OPCIONAL'


ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))

