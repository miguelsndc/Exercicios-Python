str = "O Brasil é o o o o o pais do futebol, O Brasil é penta."
lista1 = str.split(' ')
lista2 = str.split(',')
palavra = ''
contagem = 0
for bvalor in lista1:
    vezes = lista1.count(bvalor)

    if vezes > contagem:
        contagem = vezes
        palavra = bvalor

print(F'A palavra que apareceu mais vezes é Brasil ({contagem}x)')
