## O que são?
# Permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

## If
# Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

saldo = 2000.0
saque = float(input("Informe o valor de saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente! ")

## If/else
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as plavras reservadas if e else. Como sabemos, se a expressão lógica testada no if for verdadeira, então o bloco de código if sera executado. Caso contrário o bloco de código else será executado.
    
if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente! ")

## If/elif/else
# Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica que será executado. Não existe um número máximo de elifs que podemos executar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato")
else:
    print("Opção inválida")

## If aninhado
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else
    
conta_normal = True
conta_universitaria = False

cheque_especial = 500
    
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar a operação!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

## If ternário
# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.
        
status = "Sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar o saque.')