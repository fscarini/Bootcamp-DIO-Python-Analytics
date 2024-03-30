# String múltiplas linhas

## São definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

nome = 'Fernando'

## É possível usar tanto aspas duplas quanto aspas simples
mensagem = f""" 
Olá meu nome é {nome},
Eu estou aprendendo Python
"""

print(mensagem)
# >>> Olá meu nome é {nome},
# >>> Eu estou aprendendo Python

print(
    f'''
    ========================== MENU ==========================

    1 - Depositar
    2 - Sacar
    0 - Sair

    Obrigado por utilizar nossos sistemas, {nome}!
    '''
      )