from abc import ABC, abstractmethod

class Conta(ABC):  #conta genérica
    def __init__(self, agência, conta, saldo):
        self._agência = agência
        self._conta = conta
        self._saldo = saldo
    
    @property
    def agência(self):
        return self._agência
    
    @property
    def conta(self):
        return self._conta
    
    #Getter e Setter de Saldo
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa de valor')
        
        self._saldo = valor
    
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do depósito precisa ser numérico')
        
        self.saldo += valor
        self.detalhes()
    

    def detalhes(self):
        print(f'Agência: {self.agência} ', end='')
        print(f'Conta: {self.conta} ', end='')
        print(f'Saldo: {self.saldo}')
    
    @abstractmethod
    def sacar(self, valor): 
        pass
