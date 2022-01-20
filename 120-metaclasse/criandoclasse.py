#type é uma metaclasse para criar classes
class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr': 'Olá Mundo'})

a = A()
# print(a.attr)
print(a.nome)