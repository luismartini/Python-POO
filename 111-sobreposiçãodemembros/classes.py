class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')
    
    def falar(self):
        print('Estou em CLIENTE')

class ClienteVIP(Cliente):  # é um cliente e é uma pessoa
    #def falar(self):
        # Pessoa.falar(self)
        # Cliente.falar(self)
        # #super().falar()  #refere-se a superclasse
        # print(f'{self.nomeclasse} está contando vantagem...')
        def __init__(self, nome, idade, sobrenome):
            # super().__init__(self, nome, idade)
            Pessoa.__init__(self, nome, idade)
            self.sobrenome = sobrenome
            # pode usar o nome da classe
        
        def falar(self):
            Pessoa.falar(self)
            Cliente.falar(self)
            print(f'{self.nome} {self.sobrenome}')