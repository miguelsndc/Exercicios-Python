#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
##abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
from time import sleep
class BombadeCombustivel():
    def __init__(self, tipo_de_combustivel='', quantidade_de_combustivel=0):
        self.valor_litro_alcool = 3.50
        self.valor_litro_gasolinha = 4.50
        self.tipo_de_combustivel = tipo_de_combustivel
        self.quantidade_de_combustivel = quantidade_de_combustivel


    def menu(self):
        print(self.linha())
        print('POSTO DE COMBUSTÍVEL'.center(42))
        print(self.linha())
        print(F'ALCOOL : {self.valor_litro_alcool:.2f}\nGASOLINA : {self.valor_litro_gasolinha:.2f} ')
        while True:
            try:
                abastecer = input('Abastecer por Litro ou por Valor [V/L] : ').strip().lower()
            except ValueError:
                print('Digite um comando Válido.')
                continue
            else:
                if abastecer == 'v':
                    self.abastercer_por_valor()
                elif abastecer == 'l':
                    self.abastecer_por_litro()
                else:
                    if abastecer == '-1':
                        print('Encerrando sistema...')
                        sleep(2)
                        exit()
                    elif abastecer == 'alterar':
                        self.alterarvalor_do_combustivel()
                    else:
                        print('Digite um comando Válido.')
                        continue


    def abastercer_por_valor(self):
        try:
            self.tipo_de_combustivel = input('Qual o tipo de combustível ? [A/G] : ').strip().lower()
        except ValueError:
            print('Digite um tipo válido.')
            self.abastercer_por_valor()
        else:
            if self.tipo_de_combustivel == 'a':
                while True:
                    try:
                        valor = float(input('Digite o valor para abastecer: '))
                    except ValueError:
                        print('Digite um valor válido')
                        continue
                    else:
                        self.quantidade_de_combustivel = valor / self.valor_litro_alcool
                        print(f'Total de {self.quantidade_de_combustivel:.2f}L , Obrigado.')
                        break
            elif self.tipo_de_combustivel == 'g':
                while True:
                    try:
                        valor = float(input('Digite o valor para abastecer: '))
                    except ValueError:
                        print('Digite um valor válido')
                        continue
                    else:
                        self.quantidade_de_combustivel = valor / self.valor_litro_gasolinha
                        print(f'Total de {self.quantidade_de_combustivel:.2f}L , Obrigado.')
                        break
            else:
                print('Digite um tipo válido.')
                self.abastercer_por_valor()
        self.menu()

    def abastecer_por_litro(self):
        try:
            self.tipo_de_combustivel = input('Qual o tipo de combustivel ? [A/G] : ').strip().lower()
        except ValueError:
            print('Digite um tipo válido.')
            self.abastecer_por_litro()
        else:
            if self.tipo_de_combustivel == 'a':
                while True:
                    try:
                        valor = float(input('Digite quantos litros para abastecer: '))
                    except ValueError:
                        print('Digite um valor válido')
                        continue
                    else:
                        self.quantidade_de_combustivel = valor * self.valor_litro_alcool
                        print(f'Total de R${self.quantidade_de_combustivel} , Obrigado.')
                        break
            elif self.tipo_de_combustivel == 'g':
                while True:
                    try:
                        valor = float(input('Digite quantos litros para abastecer: '))
                    except ValueError:
                        print('Digite um valor válido')
                        continue
                    else:
                        self.quantidade_de_combustivel = valor * self.valor_litro_gasolinha
                        print(f'Total de R${self.quantidade_de_combustivel} , Obrigado.')
                        break
            else:
                print('Digite um tipo válido.')
                self.abastecer_por_litro()
        self.menu()


    def alterarvalor_do_combustivel(self):
        try:
            valornovo = input('Quer alterar o valor de qual tipo de Combustível [A/G] : ').strip().lower()
        except:
            print('Digite um tipo válido.')
            self.alterarvalor_do_combustivel()
        else:
            if valornovo == 'a':
                while True:
                    try:
                        preco_novo_alcool = float(input('Digite o novo preço do Alcóol : '))
                    except:
                        print('Digite um valor válido.')
                        continue
                    else:
                        self.valor_litro_alcool = preco_novo_alcool
                        print(f'Novo valor do Alcóol : {self.valor_litro_alcool:.2f}')
                        self.menu()
                        return self.valor_litro_alcool
            elif valornovo == 'g':
                while True:
                    try:
                        preco_novo_gasosa = float(input('Digite o novo preço da Gasolina : '))
                    except:
                        print('Digite um valor válido.')
                        continue
                    else:
                        self.valor_litro_gasolinha = preco_novo_gasosa
                        print(f'Novo valor da Gasolina : {self.valor_litro_gasolinha:.2f}')
                        self.menu()
                        return self.valor_litro_gasolinha
            else:
                print('Digite um tipo válido.')
                self.alterarvalor_do_combustivel()
        self.menu()


    def linha(self, tam=42):
        return '-' * tam


abastecer = BombadeCombustivel()
abastecer.menu()
