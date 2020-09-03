#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
#que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
#Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
#exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
#O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.def valor_pagamento(valor_da_prestacao, dias_atraso):
def valorpagamento(valor_pagamento, dias_de_atraso):
    if dias_de_atraso <= 0:
        valor = float(input('Dinheiro recebido:'))
        if valor > valor_pagamento:
            return valor - valor_pagamento
        elif valor == valor_pagamento:
            return 0
    elif dias_de_atraso > 0:
        print(f'Valor da multa de {valor_pagamento}')
        print('Multa aplicada de 3% do valor do produto, mais 0,1% de multa por dia de atraso...')
        valor_com_multa = ((valor_pagamento * (3 / 100)) + valor_pagamento) + (dias_de_atraso * (0.1 / 100))
        print(f'Valor total de R${(valor_com_multa):.2f}.')
        pagamento = int(input('Dinheiro recebido: R$'))
        if pagamento > valor_com_multa:
            return pagamento - valor_com_multa
        elif pagamento == valor_com_multa:
            return 0


valor_da_prestacao = float(input('Digite o valor da conta: R$'))
dias_atraso = int(input('Digite o tempo de atraso. caso esteja em dia, digite 0: '))
resp = valorpagamento(valor_da_prestacao, dias_atraso)
print(f'Troco de R${resp:.2f} obrigado.')