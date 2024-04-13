# Lista para armazenar os itens
itens = []

for i in range(1, 4):
    new_item = input('Digite um item para seu inventário: ')
    itens.append(new_item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")