# d1 = {
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'Tupla'
# }

# # print('str' in d1)
# # print('valor' in d1.values())

# # for k in d1:
# #     print(k)

# for k, v in d1.items():
#     print(k, v)


clientes = {
    'cliente1' : {'nome': 'Luiz', 'sobrenome' : 'Otávio'},
    'cliente2': {'nome': 'João', 'sobrenome': 'Moreira'},
    'cliente3': {'nome': 'Maria', 'sobrenome': 'Joana'}
}

for clientes_k, clientes_v in clientes.items(): # loop para o dicionario completo
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items(): # valor do valor 
        print(f'\t{dados_k} = {dados_v}')