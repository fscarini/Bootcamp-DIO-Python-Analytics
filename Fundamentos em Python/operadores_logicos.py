# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:

# op_comparacao + op_logico + op_comparacao...N...

saldo = 3000
saque = 600
limite = 300

saldo >= saque
# >>> True

saque <= limite
# >>> False

## Operador E
saldo >= saque and saque <= limite
# >>> False

## Operador OU
saldo >= saque or saque <= limite
# >>> True

## Operador Negação
not 1000 > 1500
# >>> True (O valor booleano de saída é invertido)

## () podem ser utilizados como precedência
