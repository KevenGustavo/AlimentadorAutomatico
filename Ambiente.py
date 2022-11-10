import random

class Ambiente:
    recipienteAgua = 0
    recipienteComida = 0

    def __init__(self):
        self.recipienteAgua = random.randrange(6)
        self.recipienteComida = random.randrange(10)

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
