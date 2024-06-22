import copy
# Dicionários - dict()
dicionario = dict()
dicionario_2 = {}

pessoa = {
    'nome' : 'Wanderley',
    'idade' : 34,
    'enderecos' : [
        {'rua' : 'Rua 1', 'numero': 91},
        {'rua' : 'Rua 2', 'numero': 28}
    ]
}

nova_chave = 'altura' # Criando e add nova chave
pessoa[nova_chave] = 1.64

for chave in pessoa: # Para dictionary, o laço pega a chave.
    print(f'{chave} - {pessoa[chave]}') # O valor é tido pelo índice, pq o default é Any.
    
del pessoa[nova_chave] # Deleta uma chave do dicionário

print(pessoa.get(nova_chave, None))

# Cópia rasa - Ambas compartilham os valores de "enderecos".
pessoa_1 = pessoa.copy()
# Cópia profunda - Cada 1 possui sua própria instância de "enderecos".
pessoa_2 = copy.deepcopy(pessoa)

pessoa.update({'nome' : 'Stéphanie', 'altura' : 1.56 })
pessoa.update(nome= 'Stéphanie', altura= 1.56)

tupla = (('nome', 'Stéphanie'), ('altura', 1.56))
lista = [['nome', 'Stéphanie'], ['altura', 1.56]]

pessoa.update(tupla)
pessoa.update(lista)
