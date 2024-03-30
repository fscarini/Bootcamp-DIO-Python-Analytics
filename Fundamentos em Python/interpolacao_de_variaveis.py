# Interpolação de variáveis

## Em Python, temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é usando o metódo format e a útilma é utilizando f-strings.

## A primeira forma não é recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas duas últimas.

nome = 'Fernando' # %s - string
idade = 20 # %d - int / %f - float
profissao = 'Analista de dados'
softwares = 'Power BI, MS Excel e Linguagem Python'

pessoa = {"nome": 'Fernando', "idade": 20, "profissao": 'Analista de dados', "softwares": 'Power BI, MS Excel e Linguagem Python'}

# Old style %
print('Olá, me chamo %s! Tenho %d anos, trabalho como %s e, utilizo as seguinte ferramentas: %s.' % (nome, idade, profissao, softwares))

# Metódo format
print('Olá, me chamo {}! Tenho {} anos, trabalho como {} e, utilizo as seguintes ferramentas: {}.'.format(nome, idade, profissao, softwares))

print('Olá, me chamo {1}! Tenho {3} anos, trabalho como {0} e, utilizo as seguintes ferramentas: {2}.'.format(profissao, nome, softwares, idade))

print('Olá, me chamo {nome}! Tenho {idade} anos, trabalho como {profissao} e, utilizo as seguintes ferramentas: {softwares}.'.format(nome = nome, idade = idade, profissao = profissao, softwares = softwares))

print('Olá, me chamo {nome}! Tenho {idade} anos, trabalho como {profissao} e, utilizo as seguintes ferramentas: {softwares}.'.format(**pessoa))

# f-string
print(f'Olá, me chamo {nome}! Tenho {idade} anos, trabalho como {profissao} e, utilizo as seguintes ferramentas: {softwares}.')

## Formatar strings com f-string
PI = 3.14159

print(f'Valor de PI: {PI:.2f}')
# >>> 'Valor de PI: 3.14'

print(f'Valor de PI: {PI:5.2f}')
# >>> 'Valor de PI:      3.14'