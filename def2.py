def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não encontrada')


lista = [1,2,3,4,5]
lista1 = [10, 20, 30, 40, 50]
func(*lista, *lista1, nome='Luiz', sobrenome='Miranda', idade=30)