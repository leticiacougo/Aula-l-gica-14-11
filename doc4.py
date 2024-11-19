class animal:
    def __init__(self, nome):
        self.nome= nome

    def som (self):
        return "som do animal"
class cachorro (animal):
    def som(self):
        return"AuAu"
    
class gato (animal):
    def som(self):
        return"Miau"
    
cachorro = cachorro("Lolo")
gato = gato("Lili")

print(cachorro.nome)
print(cachorro.som())
print(gato.nome)
print(gato.som())
