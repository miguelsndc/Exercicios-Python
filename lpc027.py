#PROGRAMA ADIVINHAÇÃO DE NÚMERO QUALQUER 
import sys
from random import randint
print('Vamos jogar um jogo! Eu penso um número e você tem que adivinhar!')
print('Pensando...')
print('Você tem 3 tentativas!!')
n1 = randint(0, 5)
n2 = int(input('Ok, pode dizer:'))
if n1 == n2:
    print('Parabéns, você acertou!!')
    sys.exit()
else:
    print('Você Errou.')
print('Tenta novamente:')
n3 = int(input('2 Tentativa, pode dizer:'))
if n1 == n3:
    print('Você acertou!!')
    sys.exit()
else:
    print('Você ERROU, tente novamente:')
n4 = int(input('3 e última tentativa:'))
if n1 == n4:
    print('Você Acertou!!')
    sys.exit()
else:
    print('Você NÃO tem mais tentativas, tenha um bom dia.')
