from Agente import Agente
from Ambiente import Ambiente

ambiente = Ambiente(6,10)
alimnentador = Agente(6,10)

for x in range(4):
    alimnentador.iniciarAgente(ambiente)
    ambiente.passarTempo()
