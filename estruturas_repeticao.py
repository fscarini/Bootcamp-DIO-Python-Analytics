# O que são?
## São estruturas utilizadas para repetir um trecho de código determinado número de vezes. Esse número pode ser previamente declarado, ou determinado atráves de uma lógica.

# Comando for
## É usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um onjeto iterável.

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print()

# Função range
## Range é um função built-in do Python, ela é usada para prooduzir uma sequência de números inteiros a partir de um ínicio para um fim; Se usarmos range(i, j) será produzido:
## i, i+1, i+2, i+3, ..., j+1.
## Ele recebe três argumentos: stop(orbigatório), start (opcional) e step (opcional).


for numero in range(0, 11): # Escreva os números de 0 a 11 (sempre irá parar um número antes, nesse caso 10)
    print(numero, end='')

for numero in range(0, 51, 5): # Escreva os números de 0 a 51, pulando de 5 em 5
    print(numero, end='')

# Comando while
## O comando while é utilizado para repetir um bloco de código várias vezes enquanto uma condição atribuída ao comando for verdadeira. Faz sentido usar o while quando não sabemos o número exato de vezes que nosso código deve ser executado.
    
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))

    if opcao == 1:
        print('Sacando...')
    if opcao == 2:
        print('Exibindo o extrato...')
    else:
        print('Obrigado por usar o nosso sistema bancário, até logo!')