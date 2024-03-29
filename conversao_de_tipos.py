# Em alguns momentos é necessário converter o tipo de uma variavel para manipular de forma diferente. Por exemplo:
## Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

## Convertendo int para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

## Convertendo float para int
preco = 10.50
print(preco)

preco = int(preco)
print(preco)

## Conversão por divisão
preco = 10
print(preco)

print(preco / 2) # retorna float

print(preco // 2) # retorna int

## Numérico para string
preco = 10.5
idade = 20

print(str(preco))
print(str(idade))

# String para número

preco = '30.5'
idade = '20'

print(type(float(preco)))
print(type(int(idade)))