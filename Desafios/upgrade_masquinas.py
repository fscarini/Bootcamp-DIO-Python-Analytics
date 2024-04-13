capacidade_atual, aumento_percentual = map(int, input().split())

# TO DO: Calcule a nova capacidade do disco de Mithril
def capacidade_upgrade(capacidade, aumento):
    nova_capacidade = capacidade + (capacidade * aumento) / 100
    print(int(nova_capacidade))

# TO DO: Imprima a nova capacidade
capacidade_upgrade(capacidade_atual, aumento_percentual)