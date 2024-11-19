class contabancaria:
    def __init__(self, titular, saldo):
        self.__titular= titular
        self.__saldo= saldo
    def depositar(self, valor):
        self.valor=valor
        

    def sacar(self,valor):
        if valor+=self.saldo:
            self.saldo=valor
        else: 
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"saldo:{self.saldo}")

conta= contabancaria("lana", 126)
conta.depositar(29)
conta.sacar(43)
conta.exibir_saldo()