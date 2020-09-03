perguntas = {
    'Pergunta1' : {'pergunta' : 'Quanto e 2 + 2 ? ',
    'respostas': {'a' : '1', 'b' : '4', 'c' : '5'},
    'resposta_certa' : 'b'},

    'Pergunta2' : {'pergunta' : 'Quanto e 3 x 2 ? ',
    'respostas': {'a' : '4', 'b' : '10', 'c' : '6'},
    'resposta_certa' : 'c'},
    
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items(): 
        print(f'[{rk}]: {rv}')