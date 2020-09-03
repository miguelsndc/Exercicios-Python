#CONFEDERAÇAO DE NATACAO CATEGORIAS DE ACORDO COM IDADE
print('\033[1;30mA Confederação de Natação criou um sistema para seus atletas de acordo com a idade\033[m')
ida = int(input('\033[1;30mDigite sua idade para saber qual é sua categoria:\033[m '))

if ida <= 9:
    print('\033[1;30mEntão você possui {} anos, sua categoria é a\033[m \033[1;34mMIRIM\033[m'.format(ida))

elif 9 < ida <= 14:
    print('\033[1;30mEntão você possui {} anos, sua categoria é a\033[m \033[1;33mINFANTIL\033[m'.format(ida))

elif 14 < ida <= 19:
    print('\033[1;30mEntão você possui {} anos, sua categoria é a\033[m \033[1;32mJÚNIOR\033[m'.format(ida))

elif 19 < ida <= 20:
    print('\033[1;30mEntão você possui {} anos, sua categoria é a\033[m \033[1;31mSÊNIOR\033[m'.format(ida))

elif ida > 20:
    print('\033[1;30mEntão você possui {} anos, sua categoria é a\033[m \033[1;35mMASTER\033[m'.format(ida))

elif ida > 100:
    print('\033[1;31mIdade inválida\033[m')
else:
    print('\033[1;31mDígito INVÁLIDO\033[m')
