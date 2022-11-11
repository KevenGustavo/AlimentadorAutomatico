from Agente import Agente
from Ambiente import Ambiente

ambiente = Ambiente()
alimnentador = Agente()

for x in range(5):
    alimnentador.iniciarAgente(ambiente)
    ambiente.passarTempo()

