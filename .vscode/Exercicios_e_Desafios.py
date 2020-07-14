class Operacoes:
   def __init__(self, linha=42):
       self.linha = '-' * linha

   def par_ou_impar(self):
       numero = int(input('Digite um número : '))
       if numero % 2 == 0:
           print(f'O número informado foi {numero}, então ele é par !')
       else:
           print(f'O número informado foi {numero}, então ele é ímpar!')
       print(self.linha)

   def _soma(self):
       print('Vamos fazer mais uma brincadeira...\nMe dá dois números...')
       n1 = int(input('Digite um aqui: '))
       n2 = int(input('E o outro aqui: '))
       soma = n1 + n2
       print(f'A soma de {n1} e {n2} é {soma}, legal né ?')
       print(self.linha)

   def _media(self):
       print('Que tal agora você me dar as notas das suas atividades desse bimestre?')
       notas = []
       for c in range(1, 5):
           nota = float(input(f'Digite sua {c} nota: '))
           notas.append(nota)
       media = sum(notas) / 4
       print(f'Sua média final é de {media}')
       if media >= 6:
           print(f'Você foi aprovado!')
           print(self.linha)
       else:
           print('Você foi reprovado ;(')
           print(self.linha)

   def Conversao_de_medidas(self):
       print('Não seria legal se eu pudesse também converter metros para centímetros, né?\nEu posso!!')
       print('Me dê um valor em metros e eu o colocarei em centímetros.')
       metros = int(input('Coloque o valor aqui: '))
       conversao_pra_centimetros = metros * 100
       print(f'{metros}m\'s Convertendo para Centímetros...')
       print(f'Temos {conversao_pra_centimetros}cm\'s')
       print(self.linha)

   def Areas_Q_C(self):
       print('Vamos calcular a área de um círculo e de um quadrado, vai ser divertido. Vamos começar com o círculo.')
       raio = int(input('Coloque o raio aqui e eu direi a área do círculo: '))
       area_da_circunferencia = raio ** 2 * 3.14
       print(f'{area_da_circunferencia} essa é a área do seu círculo.')

       print('Agora a área do quadrado.')
       lado_quadrado = int(input('Coloque aqui o valor dos lados do quadrado: '))
       area_do_quadrado = lado_quadrado ** 2
       print(f'A área do seu quadrado é essa {area_do_quadrado}.')
       print(self.linha)

   def Salario(self):
       print('Sabe se você me disser quanto ganha por hora e quantas horas trabalha eu posso advinhar seu salário.')
       valor_a_receber_por_hora_trabalhada = int(input(f'Quanto você ganha por hora? '))
       horas_trabalhadas = int(input(f'E quantas horas você trabalha por dia ? '))
       salario = (valor_a_receber_por_hora_trabalhada * horas_trabalhadas) * 22
       print(f'Seu salário é R${salario}, maneiro.')
       print(self.linha)


   def Positivo_ou_negativo(self):
       print('Vamos voltar a brincar com números?')
       num = float(input(f'Me de um número e eu direi se ele é positivo ou negativo: '))
       if num > 0:
           print(f'Seu número é positivo.')
       else:
           print(f'Seu número é negativo.')
       print(self.linha)

   def Sexo(self):
       print('Você poderia me dizer seu sexo?')
       resposta = str(input(f'Coloque F- Feminino e M- Masculino: ')).strip().lower()
       if resposta == 'f':
           print('Então você é um ser humano do sexo feminino.')
       elif resposta == 'm':
           print('Então você é um ser humano do sexo Masculino.')
       else:
           print('Opa, opa, sexo inválido ? Talvez, ah deixa pra lá, é tanto gênero hoje em dia que eu nem sei mais...')
       print(self.linha)

   def Letras(self):
       print('Agora que tal brincarmos com letras, talvez as pessoas de humanas  tenham ficado confusas até aqui.')
       letra = str(input(f'Me de uma letra e lhe direi se ela é uma vogal ou consoante:'))
       if letra in 'aeiou':
           print('Isso é uma vogal.')
       else:
           print('Isto é uma consoante.')

class Bot_XF(Operacoes):
    def main(self):
        Operacao = (self.par_ou_impar(),
        self._soma(),
        self._media(),
        self.Conversao_de_medidas(),
        self.Areas_Q_C(),
        self.Salario(),
        self.Positivo_ou_negativo(),
        self.Sexo(),
        self.Letras())
       
        Operacao.__init__()



botxf = Bot_XF()
botxf.main()