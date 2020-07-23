#CALCULADOR DE IMC
print('\033[1;34mCALCUDADOR DE ÍNDICE DE MASSA CORPORAL.\033[m')
peso = float(input('\033[1;30mDIGITE SEU PESO:\033[m '))
alt = float(input('\033[1;30mDIGITE SUA ALTURA:\033[m '))
imc = peso / (alt**2)
print('\033[1;30mSEU IMC É DE {:.1f}\033[m!!'.format(imc))
if imc <= 18.5:
    print('\033[1;30mVOCÊ ESTÁ LISTADO COMO\033[m \033[1;31mABAIXO DO PESO IDEAL\033[m')
elif 18.5 < imc < 25:
    print('\033[1;30mVOCÊ ESTÁ LISTADO COMO\033[m \033[1;34mDENTRO DO PESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[1;30mVOCÊ ESTÁ LISTADO COMO\033[m \033[0;31mSOBRE PESO\033[m')
elif 30 <= imc < 40:
    print('\033[1;30mVOCÊ ESTÁ LISTADO COMO\033[m \033[1;31mOBESO(A)\033[m')
elif imc > 40:
    print('\033[1;30mVOCÊ ESTÁ LISTADO COM UMA SITUAÇÃO DE\033[m \033[1;31mOBESIDADE MÓRBIDA!! CUIDADO!!\033[m')

