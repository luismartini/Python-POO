'''
Associação - usa | agregação - Tem | composição - é dono | herança - é

herança é de baixo para cima!!!!
'''
class Pessoa:  #superclasse  define os métodos mais genéricos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f' {self.nomeclasse} está falando...')

class Cliente(Pessoa):  #cliente herda de pessoa | Subclasse | especializado
    def comprar(self):
        print(f' {self.nomeclasse} está comprando...')

class Aluno(Pessoa):  #cliente herda de pessoa | Subclasse
    def estudar(self):
        print(f' {self.nomeclasse} está estudando...')