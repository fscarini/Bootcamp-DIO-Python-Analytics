quantidade_passos = int(input('Olá, Explorador! Digite quantos passos você irá dar para continuar sua jornada: '))

if quantidade_passos < 0:
  print('Por favor, digite um número maior do que zero!')
elif quantidade_passos == 0:
  print('Nenhum passo dado na floresta.')
else: 
  print('Explorador: 1 passo')
  for passo in range(2, quantidade_passos + 1):
    print(f'Explorador: {passo} passos')