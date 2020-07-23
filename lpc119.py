meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Maio',
         'Junho',
         'Julho'
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

data = input('Informe a data(dd/mm/aaaa): ')
print(data.split("/")[0], 'de', meses[int(data.split("/")[1])-1], data.split("/")[2])


