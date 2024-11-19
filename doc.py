class pessoa:

    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade

    def exi_informacoes(self):
        print(f"Nome:{self.nome}, Idade:{self.idade}")

p1= pessoa("Mary", 90) 
p2= pessoa("lana", 87)
p1.exi_informacoes()
p2.exi_informacoes()       