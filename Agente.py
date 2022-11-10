class Agente:

    def __init__(self):
        pass

    def sensorAgua(self, ambiente):
        if (ambiente.getRecipienteAgua() < 3):
            return True
        else:
            return False
    
    def sensorComida(self, ambiente):
        if (ambiente.getRecipienteComida() < 5):
            return True
        else:
            return False

    def atuadorAgua(self, ambiente, num):
        ambiente.setRecipienteAgua(num)

    def atuadorComida(self, ambiente, num):
        ambiente.setRecipienteComida(num)
    
    def iniciarAgente(self, ambiente):
        AguaRecipiente = ambiente.getRecipienteAgua()
        ComidaRecipiente = ambiente.getRecipienteComida()

        print("Peso do recipiente da Agua =",AguaRecipiente)
        print("Peso do recipiente da Comida =",ComidaRecipiente)

        if(self.sensorAgua(ambiente)):
            print("Ação: encher recipiente da Agua")
            self.atuadorAgua(ambiente,6)
        else:
            print("Ação: recipiente da agua cheio, não fazer nada")
            
        
        if(self.sensorComida(ambiente)):
            print("Ação: encher recipiente da Comida")
            self.atuadorComida(ambiente,10)
        else:
            print("Ação: recipiente da comida cheio, não fazer nada")
              
    