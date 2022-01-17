from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupança

banco = Banco()
cliente1 = Cliente('Luís', 44)
cliente2 = Cliente('Jonice', 54)
cliente3 = Cliente('Dudu', 12)

conta1 = ContaCorrente(1111, 254136, 0)
conta2 = ContaPoupança(2222, 254137, 0)
conta3 = ContaCorrente(1212, 254138, 0)

cliente1.inserirConta(conta1)
cliente2.inserirConta(conta2)
cliente3.inserirConta(conta3)

banco.inserirCliente(cliente1)
banco.inserirContas(conta1)

banco.inserirCliente(cliente2)
banco.inserirContas(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(10)
    cliente1.conta.sacar(5)
else:
    print('Cliente não autenticado!')