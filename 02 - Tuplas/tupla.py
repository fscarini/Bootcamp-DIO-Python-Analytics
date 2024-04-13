# Criando Tuplas - Irmã da lista

## Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula e parenteses.

frutas = ('laranja', 'pera', 'uva',)

letras = tuple('python')
numeros = tuple([1, 2, 3, 4])

pais = ('Brasil',)

## Acesso direto igual ao de uma lista convencional

frutas[0] # laranja
frutas[2] # uva
frutas[-1] # uva

# Tuplas aninhadas
## Podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso, podemos criar estruturas bidimensionais (tabelas), e acessar informações informando os índices de linha e coluna.

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

## Possuem a mesma lógica para fatiamento, ().count, ().index e len.