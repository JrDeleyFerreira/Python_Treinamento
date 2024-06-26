from itertools import combinations, permutations, product, groupby
from functools import reduce, partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# --------------------------------------------------------
# Combinação, Permutação e Produto
lista_nomes = [
    'Wanderley', 'Márcia', \
    'Rafael', 'Isabelle', 'Cíntia'
]
print_iter(combinations(lista_nomes, 2))
print_iter(permutations(lista_nomes, 2))

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminina']
]
print_iter(product(*camisetas))

# --------------------------------------------------------
# Agrupamento com groupby()
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

# alunos_ordenados = sorted(alunos, key= lambda a: a['nota'])
alunos_ordenados = sorted(alunos, key= ordena)
agrupamento = groupby(alunos_ordenados, key= ordena)

for chave, grupo in agrupamento:
    print(chave)
    for aluno in grupo:
        print(aluno)

# --------------------------------------------------------
# Mapeamento com map()
list_produtos = [
    {'nome' : 'Produto 4', 'preco' : 19.25},   
    {'nome' : 'Produto 1', 'preco' : 9.25},   
    {'nome' : 'Produto 5', 'preco' : 11.8},   
    {'nome' : 'Produto 2', 'preco' : 110.7},   
    {'nome' : 'Produto 3', 'preco' : 27.30},   
]

def muda_preco(produto):
    return {
        **produto, 
        'preco' : round(produto['preco'] * 1.1, 2)}

novos_produtos =list(map(
    muda_preco,
    list_produtos
))

print_iter(novos_produtos)

# --------------------------------------------------------
# Filtro com filter()
produtos_filtrados = filter(
    lambda prd: prd['preco'] > 30,
    list_produtos
)
print_iter(produtos_filtrados)

# --------------------------------------------------------
# Filtro com filter()
def funcao_reduce(acumulador, produto):
    return acumulador + produto['preco']

totalizador = reduce(
    # lambda ac, p: ac + p['preco'],
    funcao_reduce, # Função
    list_produtos, # Iterável
    0.0 # Acumulador
)
print('Total: %.2f' % (totalizador))
