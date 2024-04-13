# Positional, Keywords e Híbrido - Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

# positional only
# Todos os parâmetros antes da /, são apenas por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'BAC-1985', marca = 'Fiat', motor = '1.0', combustivel = "Gasolina") 

# keyword only
# Todos os parâmetros depois do *, são apenas por chaves
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo = 'Palio', ano =  1999, placa = 'BAC-1985', marca = 'Fiat', motor = '1.0', combustivel = "Gasolina") 

# Objetos de primeira clase - Em Python, tudo é objeto, dessa forma funções também são obejtos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados e usar como valor de retorno apra uma função.

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20

# Escopo local e global - Dentro do bloco da função, o escopo é local. Portanto alterações ali feitas em feitas em objetos imutáveis serão perdidas quando o método terminar de ser exucutada. Para usar objetos globais utilizamos a palavra-chave global, que informa ao itnerpretador que a variável está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser evitada.

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(800)