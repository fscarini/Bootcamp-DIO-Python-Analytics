# Metodo clear

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 22},
    "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}
}

contatos.clear()
contatos # {}

# ---------------------------------------------------------------------------------
# Metodo copy

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 22},
    "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}
}

copia = contatos.copy()
copia["fecarini@gmail.com"] = {"nome": "Fe"}

contatos["fecarini@gmail.com"] # {"nome": "Fernando", "idade": 20}
copia["fecarini@gmail.com"] # {"nome": "Fe"}

# ---------------------------------------------------------------------------------
# Metodo fromkeys - Cria uma chave no dicionário ou cria um conjunto de chaves com um valor padrao

dict.fromkeys(['nome', 'telefone']) # {'nome': None, 'telefone': None}
dict.fromkeys(['nome', 'telefone'] 'vazio') # {'nome': 'vazio', 'telefone': 'vazio'}

# ---------------------------------------------------------------------------------
# Metodo get

contatos = {
    "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}
}

contatos['chave'] # KeyError

contatos.get('chave') # None
contatos.get('chave', {}) # {} --> valor default caso o valor não seja retornável
contatos.get('fecarini@gmail.com', {}) # "fecarini@gmail.com": {"nome": "Fernando", "idade": 20}