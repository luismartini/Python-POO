from random import randint

class Pessoa:
    anoAtual = 2022  #atributo da classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def getAnoNascimento(self):  #instância
        print(self.anoAtual - self.idade)
    
    @classmethod  #decorador  #não preciso da instância, mas preciso da classe
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)
    
    #métodos estáticos - não usa nem classe nem instância
    @staticmethod
    def geraID():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.porAnoNascimento('Luís', 1977)
# p1 = Pessoa('Luís', 44)
print(p1)
print(p1.nome, p1.idade)
p1.getAnoNascimento()
print(Pessoa.geraID())
print(p1.geraID())