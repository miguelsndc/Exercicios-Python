num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#isnumeric // isdigit // isdecimal
# numeros e positivos (122212.131)

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1 + num2)
# else:
#     print('Não pude efetuar as operações.')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('ERROR')