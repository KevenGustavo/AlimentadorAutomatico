import random

class Ambiente:
    recipienteAgua = 0
    recipienteComida = 0

    def __init__(self, numAgua, numComida):
        self.recipienteAgua = random.randrange(numAgua)
        self.recipienteComida = random.randrange(numComida)

    def getAmbienteTotal(self):
        print("Recipiente de Agua =",self.recipienteAgua)
        print("Recipiente de Comida =",self.recipienteComida)
          
    def setRecipienteAgua(self, num):
        self.recipienteAgua= num
    
    def setRecipienteComida(self, num):
        self.recipienteComida= num

    def getRecipienteAgua(self):
        return self.recipienteAgua
    
    def getRecipienteComida(self):
        return self.recipienteComida

    def passarTempo(self):
        print("\n-=Passando o tempo no ambiente=-")
        self.recipienteAgua -= random.randrange(self.recipienteAgua)
        self.recipienteComida -= random.randrange(self.recipienteComida)
