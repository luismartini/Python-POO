class Banco:
    def __init__(self):
        self.agência = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []
    
    def inserirCliente(self, cliente):
        self.clientes.append(cliente)
    
    def inserirContas(self, conta):
        self.contas.append(conta)
    
    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agência not in self.agência:
            return False
        return