## Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

age = 20
name = 'Fernando'
print(f'Meu nome é {name}, e eu tenho {age} anos!')


age, name = (18, 'Leôncio') # Inline
print(f'Meu nome é {name}, e eu tenho {age} anos!')

## Perceba que não precisamos definir o tipo de dado da variável, o Python faz isso de forma automática. Por isso, não podemos criar uma variável sem atribuir um valor para a mesma.

## São utilizadas para armazenar valores, e seu valor é imutável, ou seja, não pode ser alterado ao decorrer do programa. Ex: uma vez que age = 20, ele iria terminar a execução sendo igual a 20.

## Não existe constante em Python! Usamos uma convenção que diz ao programador que a variável é uma constante, para fazer isso, devemos criar uma variável com o nome em letras maísculas.

ABS_PATH = '/home/FeCarini/Documents/python_course'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG'
]
PI = 3.14

# Boas práticas
## O padrão de nomes deve ser em snake case: Um valor separado por espaço em branco, deve ser substituído por _
## Escolher nomes sugestivos
## Nome de constantes todo em maíusculo (também seguem o padrão em snake_case)

