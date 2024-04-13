# O que são?
## É um bloco de código identificado por nome e pode receber uma lista de parâmetros, estes podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento do código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada. 

def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Seja bem-vindo {nome}!')

def exibir_mensagem_3(nome="Anônimo"):
    print(f'Seja bem-vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2(nome = 'Fernando')
exibir_mensagem_3()
exibir_mensagem_3(nome = 'Charles')

# Retornando valores
## Para retornar um valor, utilizamos a palavra reservada return. Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, numero, sucessor

def func_3():
    print('Olá, Mundo!')

print(calcular_total([16, 20, 31])) # 67
print(retorna_antecessor_e_sucessor(5)) # 4, 5, 6
print(func_3) # None
func_3() # 'Olá, Mundo!'

# Argumentos nomeados
## Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f'Carro inserido na base de dados com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat', 'Palio', 1999, 'ABC-1994')
salvar_carro(marca ='Fiat', modelo = 'Palio', ano = 1999, placa = 'ABC-1744')
salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1698'})

# Args e kwargs
## Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n.join(args)'
    meta_dados = '\n'.join([f"{chave.title()}: {valor} for chave, valor in kwargs.items"])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Sexta-feira, 12 de Abril de 2024', 'Zen of Python', 'Beautiful is better than ugly.', autor = 'Tim Peters', ano = 1999)
