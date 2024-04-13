# Criando dicionários
## É um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. 

dados = {"nome" : "Fernando", "idade" : 20, "telefone" : "11 95870-8287"}

dados["nome"] # Fernando
dados["idade"] # 20
dados["telefone"] # 11 95870-8287

dados["nome"] = 'Robert' # Mudança dos dados dentro do dicionário
dados["idade"] = 22
dados["telefone"] = "11 96451-7236"

# Dicionários aninhados
## Podemos armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável (string e números).

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 22},
    "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}
}

contatos["fecarini@gmail.com"]["nome"] # "Fernando"

# Iterando dicionários
## A forma mais comum de percorrer dados de um dicionário é utilizando o comando for

for chave in contatos:
    print(chave, contatos[chave])

# Ou

for chave, valor in contatos.items():
    print(chave, valor)

# "guilherme@gmail.com": {"nome": "Guilherme", "idade": 22}
# "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}