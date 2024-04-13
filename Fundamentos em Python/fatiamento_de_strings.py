# Fatiamento de strings

## É uma técnica utilizada para retornar substrings(partes da string original), informado início(start), fim(stop) e passo(step): [start:stop:step]

nome = 'Fernando Silva Carini'

print(nome[0])
# >>> 'F'

print(nome[:8])
# >>> 'Fernando'

print(nome[9:])
# >>> 'Silva Carini'

print(nome[9:15])
# >>> 'Silva'

print(nome[9:15:2])
# >>> 'Sla'

print(nome[:])
# >>> 'Fernando Silva Carini'

print(nome[:: - 1])
# >>> 'iniraC avliS odnanreF'
