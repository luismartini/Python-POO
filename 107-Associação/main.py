'''
Relação entre classes

Associação - uma classe se associa a outra, mas são independentes.
Associação mais fraca
'''
from classes import Escritor, Caneta, MáquinaDeEscrever

escritor = Escritor('Jonice')  #escritor = objeto
caneta = Caneta('Bic')
máquina = MáquinaDeEscrever()

# escritor.ferramenta = caneta
escritor.ferramenta = máquina
escritor.ferramenta.escrever()

del escritor
# print(escritor)
print(caneta.marca)
máquina.escrever()