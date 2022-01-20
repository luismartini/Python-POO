""" 
Context Manager 
"""
'''
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)
    
    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo
    
    def __exit__(self, exc_val, exc_type, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # tratei a exceção
        return True
        
        
with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.hashsh('Alguma coisa')
'''
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo')
        yield arquivo 
    finally:
        print('Fechando arquivo')
        arquivo.close()

#deve ser usado sempre!
with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')