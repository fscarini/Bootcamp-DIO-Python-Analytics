# Métodos da classe list

## [].append -> Adiciona um novo elemento na lista
lista = []
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

## [].clear -> Limpa a lista
lista_clear = [1, 'Python', [40, 30, 20]]
lista_clear.clear()

print(lista_clear) # []

## [].copy -> Faz uma cópia da lista, não afetando a lista original
lista_copy = [1, 'Python', [40, 30, 20]]
lista_copiada = lista_copy.copy()
lista_copy = [2, 'Java', [70, 60, 50]]

print(lista_copiada) # [1, 'Python', [40, 30, 20]]
print(lista_copy) # [2, 'Java', [70, 60, 50]]
print(id(lista_copy), id(lista_copiada))

## [].count -> Conta quantas vezes um objeto aparece dentro da lista
cores = ['vermelho', 'azul', 'verde', 'azul']

cores.count('vermelho') # 1
cores.count('azul') # 2
cores.count('verde') # 1

## [].extend -> Adiciona um elemento no final da lista
linguagens = ['Python', 'JavaScript', 'C']
print(linguagens) # ['Python', 'JavaScript', 'C']

linguagens.extend(['Java', 'C#'])
print(linguagens) # ['Python', 'JavaScript', 'C', 'Java', 'C#']

## [].index -> Qual o id do objeto dentro da lista
linguagens_index = ['Python', 'JavaScript', 'C', 'Java', 'C#', 'C']

linguagens_index.index('Java') # 3
linguagens_index.index('Python') # 0
linguagens_index.index('C') # 2 -> Retorna somente a primeira instância do elemento dentro da lista

## [].pop -> Remove o último elemento da lista, ou o elemento especificado como argumento
linguagens_pop = ['Python', 'JavaScript', 'C', 'Java', 'C++']

linguagens_pop.pop() # ['Python', 'JavaScript', 'C', 'Java']
linguagens_pop.pop() # ['Python', 'JavaScript', 'C']
linguagens_pop.pop() # ['Python', 'JavaScript']
linguagens_pop.pop(0) # Remove 'Python' -> ['JavaScript']

## [].remove -> Remove elementos de uma lista, usando como argumento o elemento
linguagens_remove = ['Python', 'JavaScript', 'C', 'Java', 'C++']
linguagens_remove.remove('Python') # ['JavaScript', 'C', 'Java', 'C++']

## [].reverse -> Espelha a lista
frutas = ['laranja', 'pera', 'maçã', 'uva', 'morango']

frutas.reverse() # ['morango', 'uva', 'maçã', 'pera', 'laranja']

## [].sort -> Ordena a lista de forma alfabética, também pode ser passado um argumento
frutas_sort = ['laranja', 'pera', 'maca', 'uva', 'morango']
frutas_sort.sort() # ['laranja', 'maca', 'morango', 'pera', 'uva']

frutas_sort = ['laranja', 'pera', 'maca', 'uva', 'morango']
frutas_sort.sort(reverse = True) # ['uva', 'pera', 'morango', 'maca', 'laranja']

frutas_sort = ['laranja', 'pera', 'maca', 'uva', 'morango']
frutas_sort.sort(key = lambda x: len(x)) # ['uva', 'pera', 'maca', 'laranja', 'morango'] -> Tamanho das palavaras do menor para o maior

frutas_sort = ['laranja', 'pera', 'maca', 'uva', 'morango']
frutas_sort.sort(key = lambda x: len(x), reverse = True) # ['laranja', 'morango', 'pera', 'maca', 'uva'] -> Tamanho das palavaras do maior para o menor

## len -> Tamanho da lista
carros = ['gol', 'fusca', 'brasilia', 'palio', 'corsa', 'voyage', 'fiesta']
len(carros) # 7

## sorted -> Ordena iteráveis assim como o [].sort
carros = ['gol', 'fusca', 'brasilia', 'palio', 'corsa', 'voyage', 'fiesta']

print(sorted(carros, key = lambda x:len(x)))

print(sorted(carros, key = lambda x:len(x), reverse = True))