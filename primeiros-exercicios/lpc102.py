class perifecos():
    def __init__(self, fone, mouse, teclado, monitor,):
        self.fone = fone
        self.mouse = mouse
        self.teclado = teclado
        self.monitor = monitor


class specdopc():
    def __init__(self, processador, memoria_ram, placa_de_video, fonte):
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.fonte = fonte

    def exibirspecsdopc(self):
        print(self.processador, self.memoria_ram, self.placa_de_video, self.fonte)

specs1 = specdopc('Ryzen 3 2200g\n', '8gb\n', 'Vega 8\n', '600w\n')
print(specs1.processador, specs1.memoria_ram, specs1.placa_de_video, specs1.fonte )
perifecosdomeupc = perifecos('Razer Kraken\n', 'Mouse Logitech\n', 'Tecladao multilaser da massa\n', 'TV Monitor LG')
print(perifecosdomeupc.fone, perifecosdomeupc.mouse, perifecosdomeupc.teclado, perifecosdomeupc.monitor)
print('-' * 40)
