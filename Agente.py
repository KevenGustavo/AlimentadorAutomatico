class Agente:

    def __init__(self, numAgua, numComida):
        self.valorMaxAgua = numAgua
        self.valorMaxComida = numComida

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
        print("-Valor após encher o recipiente de agua =",ambiente.recipienteAgua)

    def atuadorComida(self, ambiente, num):
        ambiente.setRecipienteComida(num)
        print("-Valor após encher o recipiente de comida =",ambiente.recipienteComida)
    
    def iniciarAgente(self, ambiente):
        
        print("\n#Recipiente da Agua:")
        if(self.sensorAgua(ambiente)):
            print("-Ação: Recipiente abaixo do limite, encher recipiente da Agua")
            self.atuadorAgua(ambiente,self.valorMaxAgua)
        else:
            print("-Ação: Recipiente acima do limite, não fazer nada")
        
        print("#Recipiente de Comida:")
        if(self.sensorComida(ambiente)):
            print("-Ação: Recipiente abaixo do limite, encher recipiente da Comida")
            self.atuadorComida(ambiente,self.valorMaxComida)
        else:
            print("-Ação: Recipiente acima do limite, não fazer nada")
              
    