from abc import ABC, abstractmethod

class Contas(ABC):
    def __init__(self, agência, conta, saldo):
        self.agência = agência
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'{self.agência} '
              f'{self.conta}'
              f'{self.saldo}')
    
    @abstractmethod
    def sacar(self): pass

class ContaPoupança(Contas):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Contas):
    def __init__(self, agência, conta, saldo, limite=100):
        super().__init__(agência, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()