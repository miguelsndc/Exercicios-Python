numbers = []
#pegando inputs
for index in range(1, 21):
  n = int(input(f'Digite o {index}º número: ')) 
  numbers.append(n)
#separando os valores par/impar
impares = [number for number in numbers if number % 2 == 0]
pares = [number for number in numbers if number % 2 != 0]
#organizando a lista
numbers = sorted(numbers)
impares = sorted(impares)
pares = sorted(pares)

print(f'Números: {numbers}\n Pares: {impares}\n ímpares: {pares}')