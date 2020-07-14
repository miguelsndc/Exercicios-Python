def func(*args, **kwargs):
    print(args)
    print(kwargs)
    idade = kwargs.get('idade')
    if idade != None:
        print(idade)
    else:
        print('Não foi possível encontrar a idade.')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome = 'Miranda', idade = 30)
