'''
Em Python, tudo é um objeto: incluindo classes
Metaclasses são as "classes" que criam classes
type é uma metaclasse
'''
'''
a #objetos = A() 
b = A()  #instâncias da classe
c = A()
'''
'''
criar metaclasse
'''
class Meta(type):
    # bases é classes pai que serão criadas
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        print(f'{name} tentou sobrescrever')
        if 'attr_class' in namespace:
            del namespace['attr_classe']
        
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):  #criar bibliotecas
    attr_classe = 'Valor A'

class B(A):  #criar interface
    atrr_classe = 'Valor B'

class C(B):
    atrr_classe = 'Valor C'

c = C()
print(c.atrr_classe)