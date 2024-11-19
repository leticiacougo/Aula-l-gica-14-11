class carro:
    def __init__(self, marca, modelo, ano):
        self.marca= marca
        self.modelo= modelo
        self.ano= ano
    def exibir_detalhes(self):
        print(f"marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}")
c1= carro("toyota","palio", 2010)
c2= carro("fiat", "uno", 2008)
c1.exibir_detalhes()
c2.exibir_detalhes()