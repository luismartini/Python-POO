from eletrônico import Eletrônico
from log import LogMixin    

class Smartphone(Eletrônico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)  #chamou o construtor da classe Pai
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.logError(error)
            return
        
        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO'
            print(error)
            self.logError(error)
            return
        
        info = f'{self._nome} ESTÁ CONECTADO'
        print(info)
        self.logInfo(info)
        self._conectado = True
    
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO'
            print(error)
            self.logError(error)
            return
        
        info = f'{self._nome} FOI DESLIGADO'
        print(info)
        self.logInfo(info)
        self._conectado = False