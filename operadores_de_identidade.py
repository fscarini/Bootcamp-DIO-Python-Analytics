# São operadores utilizados para comparar se os dois objetos comparados testados ocupam a mesma posição na memória

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
# >>> True (Foi feita a comparação com o objetivo de saber se as duas variáveis ocupam o mesmo espaço na memória)

print(curso is not nome_curso)
# >>> False

print(saldo is limite)
# >>> True