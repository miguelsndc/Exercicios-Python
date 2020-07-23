#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
a = list()
while True:
    n = float(input('Digite um valor: '))
    a.append(n)
    if n == -1:
        break
m = sum(a) / len(a)
a.pop(-1)
print(f'Foram informados {len(a)} Valores.')
print(f'Os Valores informados foram {a}.')
a.sort(reverse= True)
print(f'A lista, Invertida é {a}')
print(f'A soma deles é {sum(a)}')
print(f'A média desses valores é {m:.2f}')
for i, l in enumerate(a):
    if l > m:
        print(f'O valor {l} é maior que a média dos mesmos.')
print('<<< VOLTE SEMPRE >>>')