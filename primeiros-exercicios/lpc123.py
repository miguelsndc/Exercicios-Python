from sys import exit
class bombaCombustivel():
    def __init__(self, tipo_de_combustivel='', valor_litro=0, quantidade_de_combustivel=0):
        self.valor_litro = valor_litro
        self.quantidade_de_combustivel = quantidade_de_combustivel
        self.tipo_de_combustivel = tipo_de_combustivel
        self.alcool = 3.50
        self.gasolina = 4.50

    def linha(self, tam=42):
        return '-' * tam

    def menu(self):
        print(self.linha())
        print('POSTO DE COMBUSTÍVEL'.center(42))
        print(self.linha())
        print(f'ALCOOL : R$ {self.alcool:.2f}\nGASOLINA : R${self.gasolina:.2f}')
        while True:
            try:
                tipo = input('Gostaria de abastecer por litro ou por valor ? (Digite alt para alterar algum valor) ou -1 para finalizar.').strip().lower()
            except ValueError:
                print('Digite algo válido.')
                continue
            else:
                if tipo == 'v':
                    self.abastecerPorValor()
                elif tipo == 'l':
                    self.abastecerPorLitro()
                elif tipo == '-1':
                    print('Desligando o sistema...')
                    exit()
                elif tipo == 'alt':
                    self.alterar_preco()
                else:
                    print('Digite apenas [L/V] ')
                    continue


    def abastecerPorValor(self):
        try:
            self.tipo_de_combustivel = input('Tipo de Combustível: [A/G] ').strip().lower()
        except ValueError:
            print('Digite um valor válido.')
            self.abastecerPorValor()
        else:
            while self.tipo_de_combustivel not in 'ag':
                print('Digite um tipo válido.')
                self.abastecerPorValor()

            if self.tipo_de_combustivel == 'a':
                while True:
                    try:
                        dinheiro = float(input('Digite o valor a ser abastecido: R$').strip().lower())
                    except ValueError:
                        print('Digite um valor válido.')
                        continue
                    else:
                        total_litro = dinheiro / self.alcool
                        print(f'Total de litros : {total_litro}L')
                        break
            elif self.tipo_de_combustivel == 'g':
                while True:
                    try:
                        dinheiro = float(input('Digite o valor a ser abastecido: R$').strip().lower())
                    except ValueError:
                        print('Digite um valor válido.')
                        continue
                    else:
                        total_litro = dinheiro / self.gasolina
                        print(f'Valor a ser pago : R${total_litro}')
                        break
        self.menu()

    def abastecerPorLitro(self):
        try:
            self.tipo_de_combustivel = input('Tipo de Combustível: [A/G] ').strip().lower()
        except ValueError:
            print('Digite algo válido.')
            self.abastecerPorLitro()
        else:
            while self.tipo_de_combustivel not in 'ag':
                print('Digite um tipo de combustível válido [A/G] ')
                self.abastecerPorLitro()
            if self.tipo_de_combustivel == 'a':
                while True:
                    try:
                        litros = float(input('Digite a Quantidade de Litros: '))
                    except ValueError:
                        print('Digite algo válido.')
                        continue
                    else:
                        total_reais = litros * self.alcool
                        print(f'Valor a ser pago: R${total_reais}')
                        break
            elif self.tipo_de_combustivel == 'g':
                    while True:
                        try:
                            litros = float(input('Digite a Quantidade de Litros: '))
                        except ValueError:
                            print('Digite algo válido.')
                            continue
                        else:
                            total_reais = litros * self.gasolina
                            print(f'Valor a ser pago: R${total_reais}')
                            break
        self.menu()

    def alterar_preco(self):
        print(self.linha())
        print('ALTERAR PREÇOS'.center(42))
        print(self.linha())
        while True:
            try:
                tipo_alt = input('Alterar preço de qual tipo de combustível ? [A/G] ').strip().lower()
            except ValueError:
                print('Digite um tipo válido.')
                continue
            else:
                if tipo_alt == 'a':
                    novo_valor_alcool = float(input('Digite o novo valor do Alcoól : R$'))
                    self.alcool = novo_valor_alcool
                    print(f'Novo valor do alcool : R${self.alcool}')
                    while True:
                        try:
                             new_alt = input('Gostaria de alterar novamente ? [S/N] ').strip().lower()
                        except ValueError:
                            print('Digite apenas S ou N.')
                            continue
                        else:
                            if new_alt == 's':
                                self.alterar_preco()
                            elif new_alt == 'n':
                                self.menu()
                                break
                            else:
                                print('Digite apenas S ou N.')
                                continue
                elif tipo_alt == 'g':
                    novo_valor_gasolinha = float(input('Digite o novo valor da Gasolina : R$'))
                    self.gasolina = novo_valor_gasolinha
                    print(f'Novo valor da Gasolina : R${self.gasolina}')
                    while True:
                        try:
                             new_alt = input('Gostaria de alterar novamente ? [S/N] ').strip().lower()
                        except ValueError:
                            print('Digite apenas S ou N.')
                            continue
                        else:
                            if new_alt == 's':
                                self.alterar_preco()
                            elif new_alt == 'n':
                                self.menu()
                                break
                            else:
                                print('Digite apenas S ou N.')
                                continue
                else:
                    print('Digite um tipo válido: ')
                    continue
        self.menu()




posto = bombaCombustivel()
posto.menu()
