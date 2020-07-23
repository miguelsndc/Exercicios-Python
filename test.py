#Classe Quadrado: Crie uma classe que modele um quadrado:
#
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self, valor_do_lado=0):
        self._valor_do_lado = valor_do_lado

    def main(self, perimetro=0, area=0):
        self.perimetro = perimetro
        self.area = area
        try:
            self._valor_do_lado = float(input('Digite o valor do lado do Quadrado: '))
        except:
            print('Digite um valor válido.')
            self.main()
        else:
            print(f'O valor do lado do Quadrado é {self._valor_do_lado}')
            print('(P para Perímetro, A para Área, M para mudar o valor do lado e S para saber o valor Atual do Lado.')
            self.Operacoes()


    def Operacoes(self):
        while True:
            try:
                calculos = str(input('Qual operação gostaria de fazer com o Quadrado? [P/A/M/S]')).strip().lower()
            except:
                print('Digite apenas P ou A')
                continue
            else:
                while True:
                    if calculos == 'p':
                        self.perimetro = self._valor_do_lado * 4
                        print(f'Perimetro do Quadrado : {self.perimetro}')
                        break
                    elif calculos == 'a':
                        self.area = self._valor_do_lado ** 2
                        print(f'Area do Quadrado : {self.area}')
                        break
                    elif calculos == 'm':
                        while True:
                            try:
                                novo_valor_do_lado = float(input('Digite o novo valor do Lado do Quadrado: '))
                                self._valor_do_lado = novo_valor_do_lado
                            except ValueError:
                                print('Digite um Valor válido.')
                                continue
                            else:
                                print(f'Valor do lado do Quadrado : {self._valor_do_lado}')
                                self.Operacoes()
                                break
                    elif calculos == 's':
                        print(f'Valor atual do Lado : {self._valor_do_lado}')
                        self.Operacoes()
                        break

                    else:
                        print('Digite apenas P ou A.')
                        continue


quraddo = Quadrado()
quraddo.main()

