# Vamos entender o funcionamento da estrutura de dados set
## É uma coleção que não possui objetos repetidos, usamos sets para representar conjunto matemáticos ou eliminar itens duplicados de um iterável.

set([1, 2, 3, 1, 3, 4]) # (1, 2, 3, 4)

set('abacaxi') # {'b', 'a', 'c', 'x', 'i'}

set(('palio', 'gol', 'celta', 'palio')) # {'gol', 'celta', 'palio'}

# Acessando os dados
## Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

numeros = {1, 2, 3, 2}

numeros = list(numeros)

# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # Junta os dois conjuntos

# {}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # Deixa apenas os elementos em comum

# {}.difference
conjunto_a.difference(conjunto_b) # 1
conjunto_b.difference(conjunto_a) # 4
# O que tem no conjunto x que não tem no conjunto y?

# {}.symmetric_difference
conjunto_a.symmetric_difference(conjunto_b) # 1, 4
# São os elementos que não estão em intersecção

# {}.issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True, todos os elementos de A, estão contidos em B
conjunto_b.issubset(conjunto_a) # False, nem todos os elementos de B, estão contidos em A

# {}.issuperset
conjunto_a.issuperset(conjunto_b) # False, Nem todos os elementos de B, estão contidos em A
conjunto_b.issubset(conjunto_a) # True, Todos os elementos de A, estão contidos em B

# {}.isdisjoint - Não há nenhum valor em intersecção nos conjuntos

# {}.add - Se o elemento passado não existir, ele é adicionado

# {}.clear - Irá limpar seu conjunto

# {}.copy - Gera uma cópia do seu conjunto

# {}.discard - Descarta um valor

# {}.pop - Tira sempre o último valor do conjunto

# {}.remove - Remove um valor

# len - Retorna o tamanho do conjunto

# in - Verifica se um elemento está dentro do conjunto