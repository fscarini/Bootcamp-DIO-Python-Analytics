## Função input
# A função input, é utilizada quando queremos ler dados de entrada. Ela recee um argumento do tipo string, que é exibido para o usuário na saída. A função lê a entrada, converte para string e retorna o valor

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenoem: ")

# Função print
## A função print é utilizada quando queremos exibir dados na saída. Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

print(nome, sobrenome)
print(nome, sobrenome, end='... \n')
print(nome, sobrenome, sep='#')