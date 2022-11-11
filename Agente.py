class Agente:

    def __init__(self):
        pass

    def sensorAgua(self, ambiente):
        AguaRecipiente = ambiente.getRecipienteAgua()
        print("\nSensor: peso do recipiente da Agua =",AguaRecipiente)
        if (AguaRecipiente < 3):
            return True
        else:
            return False
    
    def sensorComida(self, ambiente):
        ComidaRecipiente = ambiente.getRecipienteComida()
        print("\nPeso do recipiente da Comida =",ComidaRecipiente)
        if (ComidaRecipiente < 5):
            return True
        else:
            return False

    def atuadorAgua(self, ambiente, num):
        ambiente.setRecipienteAgua(num)

    def atuadorComida(self, ambiente, num):
        ambiente.setRecipienteComida(num)
    
    def iniciarAgente(self, ambiente):

        if(self.sensorAgua(ambiente)):
            print("Ação: recipiente abaixo do limite, encher recipiente da Agua")
            self.atuadorAgua(ambiente,6)
        else:
            print("Ação: recipiente da agua cheio, não fazer nada")
            
        if(self.sensorComida(ambiente)):
            print("Ação:  recipiente abaixo do limite, encher recipiente da Comida")
            self.atuadorComida(ambiente,10)
        else:
            print("Ação: recipiente da comida cheio, não fazer nada")
              
    