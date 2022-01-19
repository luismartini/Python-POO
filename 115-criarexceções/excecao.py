class TaErradoError(Exception):
    pass

'''
criar sua exceção personalizada
'''

def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')

    