from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['Carteira de Trabalho'] = int(input('Digite a CTPS: '))
if dados['Carteira de Trabalho'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = ((dados['Ano de Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
print('{:^60}'.format('DADOS DO TRABALHADOR'))
for k, v in dados.items():
    print(f'{k} : {v}')