from classes import Cliente  #classe Cliente está responsável pela composição 

cliente1 = Cliente('Luís', 44)
cliente1.inserirEndereço('Bauru', 'SP')
print(cliente1.nome)
cliente1.listaEndereços()
del cliente1
print()


cliente2 = Cliente('Jonice', 54)
cliente2.inserirEndereço('Mogi', 'SP')
cliente2.inserirEndereço('Rio', 'RJ')
print(cliente2.nome)
cliente2.listaEndereços()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.inserirEndereço('São Paulo', 'SP')
print(cliente3.nome)
cliente3.listaEndereços()
del cliente3
print()

print('##############################################')

