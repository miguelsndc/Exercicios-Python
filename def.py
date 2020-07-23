# #1 Questão

# def saudacao(msg, nome):
#     return f'{msg} {nome}'

# welcome = saudacao('Ola','Mundo')
# print(welcome)

# #2 Questão

# def soma(a=0, b=0, c=0):
#     return a + b + c

# sum = soma(5, 6, 1)
# print(sum)

# def plus(num, per):
#     return num + (num * (per/100))

# percentual = plus(10, 20)
# print(percentual)


#4 Questão 

def fizz_buzz(num):
    if num % 2 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 5 == 0 and num % 3 == 0:
        return 'fizzbuzz'
    else:
        return num
    
instance = fizz_buzz(5)
print(instance)