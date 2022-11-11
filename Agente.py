class Agente:

    def __init__(self):
        pass

    def sensorAgua(self, ambiente):
        AguaRecipiente = ambiente.getRecipienteAgua()
        print("-Sensor: Peso do recipiente da Agua =",AguaRecipiente)
        if (AguaRecipiente < 3):
            return True
        else:
            return False
    
    def sensorComida(self, ambiente):
        ComidaRecipiente = ambiente.getRecipienteComida()
        print("-Sensor: Peso do recipiente da Comida =",ComidaRecipiente)
        if (ComidaRecipiente < 5):
            return True
        else:
            return False

    def atuadorAgua(self, ambiente, num):
        ambiente.setRecipienteAgua(num)

    def atuadorComida(self, ambiente, num):
        ambiente.setRecipienteComida(num)
    
    def iniciarAgente(self, ambiente):
        
        print("\n#Recipiente da Agua:")
        if(self.sensorAgua(ambiente)):
            print("-Ação: Recipiente abaixo do limite, encher recipiente da Agua")
            self.atuadorAgua(ambiente,6)
        else:
            print("-Ação: Recipiente acima do limite, não fazer nada")
        
        print("#Recipiente de Comida:")
        if(self.sensorComida(ambiente)):
            print("-Ação: Recipiente abaixo do limite, encher recipiente da Comida")
            self.atuadorComida(ambiente,10)
        else:
            print("-Ação: Recipiente acima do limite, não fazer nada")
              
    