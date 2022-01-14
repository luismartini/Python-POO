'''
Variáveis de classe/atributos de classe
'''
class A:
    vc = 123  # é variável da classe. Disponível para todos
    def __init__(self):
        # self.vc = 321  #variável de instância
        pass

a1 = A()
a2 = A()
A.vc = 'Alterado'

# A.vc = 321  # mudou para todas as instâncias - inter. procura na instância... depois procura na classe
# a1.vc = 321  #

# print(a1.__dict__)  # 321 
# print(a2.__dict__)  #não tenho nada
# print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)