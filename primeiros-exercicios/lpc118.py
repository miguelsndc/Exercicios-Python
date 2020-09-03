
def numeros(num):
    n = str(num)
    return len(n)


numero = int(input('Digite um número: '))
valor = numeros(numero)
print(f'O número {numero} tem {valor} dígito(s)')
