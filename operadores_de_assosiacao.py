# São utilizados para verificar se um objeto está presente em uma sequência

curso = 'Curso de Python'
frutas = ['Laranja', 'Uva', 'Limão']
saques = [1500, 100]

print('Python' in curso)
# >>> True

print('Maçã' in frutas)
# >>> False

print('laranja' in frutas)
# >>> False (Case Sensitive)

print(1750 not in saques)
# >>> True