curso = 'PyThON'

# Maíscula, minúscula e título

## Maísucla
print(curso.upper())
# >>> PYHTON

## Minúscula
print(curso.lower())
# >>> python

## Título
print(curso.title())
# >>> Python

# Eliminando espaços em branco

curso = "    Python  "

print(curso.strip())
# >>> Python

print(curso.lstrip()) # Remove espaço da esquerda
# >>> "Python  "

print(curso.rstrip()) # Remove espaço da direita
# >>> "   Python"

# Junções e centralização

curso = "Python"

print(curso.center(10, '#')) # args: Nº de caracteres, caractere que pode ser inserido
# >>> "##Python##"

print(".".join(curso))
# >>> "P.y.t.h.o.n"