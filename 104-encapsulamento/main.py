'''
Encapsulamento: serve para esconder e proteger sua classe, atributo ou método

Modificadores de acesso:
public (dentro e fora da classe), protected (dentro da classe ou das filhas da classe), private (atributo ou método só disponível na classe).
_ -> protected: mais fraco e sutil (publico, com _)
__ -> privado: não pode ser acessado (_NOMECLASSE__nomeatributo)
'''
class BaseDeDados:
    def __init__(self, ):  #construtor
        self.__dados = {}  #.dados coração da classe
    
    @property  # liberar acesso aos valores
    def dados(self):
        return self.__dados
    
    #inserir, listar e apagar
    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def listaClientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserirCliente(1, 'Luís')
bd.inserirCliente(2, 'Luísa')
bd.inserirCliente(3, 'Jonice')
bd.inserirCliente(4, 'Adele')
# print(bd.__dados)
# print(bd._BaseDeDados__dados)
# bd.listaClientes()
# bd.dados = 'Outro valor'
print(bd.dados)