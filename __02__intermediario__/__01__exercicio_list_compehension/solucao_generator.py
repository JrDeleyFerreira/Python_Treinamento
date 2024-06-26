import copy

from dados import list_produtos

print(*list_produtos, sep='\n')
print()

# Aumentar preço em 10%
novos_produtos = [
    # Os 2 asteriscos indicam q cada item/produto da lista é 1 dict()
    {**p, 'preco' : round(p['preco'] * 1.1, 2)} # Desse dict(), pego a chave "preco"
    for p in copy.deepcopy(list_produtos) # Não precisa do deepcopy
]

print(*novos_produtos, sep='\n')
print()

# Produtos por ordem decrescente de NOME
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(list_produtos), # Não precisa do deepcopy
    key= lambda n: n['nome'],
    reverse= True
)

print(*produtos_ordenados_por_nome, sep='\n')
print()

# Produtos por ordem crescente de PREÇO
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(list_produtos),
    key= lambda p: p['preco']
)

print(*produtos_ordenados_por_preco, sep='\n')