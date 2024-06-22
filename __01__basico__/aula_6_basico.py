# Set - Conjuntos
tipo_set = set('Wanderley')
tipo_set_1 = {'Wanderley', 1, 2, 3}
tipo_set.add(('Sthéfanie', 42))

s1 = tipo_set_1.symmetric_difference(tipo_set)
s1 = tipo_set_1 ^ tipo_set

print(tipo_set)

lista = [4, 1, 1, 3, 0, 0, 2, 2]
set_list = list(set(lista))

print(set_list)
print()

# Lambda
lista_nomes = [
    {'nome' : 'Wanderley', 'idade' : 34},
    {'nome' : 'Rafael', 'idade' : 29},
    {'nome' : 'Isabelle', 'idade' : 3},
    {'nome' : 'Márcia', 'idade' : 58}
]

def exibir(lista_ordenada):
    for item in lista_ordenada:
        print(item)
    print()
# .sort() apenas ordena em tempo de execução
lista_nomes.sort(key= lambda item: item['nome'])
# sorted() cria uma cópia rasa ordenada
l1 = sorted(lista_nomes,key= lambda item: item['idade'])
exibir(lista_nomes)
exibir(l1)

# *args e *kwargs
dict_pessoa = {
    'nome' : 'Wanderley', 'sobrenome' : 'Ferreira', \
    'idade' : 34, 'altura' : 1.64}

def mostra_argumentos_nomeados(*args, **kwargs):
    print(f'Argumentos não nomeados: {args} \n')
    for chave, valor in kwargs.items():
        print(chave, valor)
    print()
        
mostra_argumentos_nomeados(1, 2, nome='Wanderley', idade=34)
mostra_argumentos_nomeados(**dict_pessoa)

verdadeiro = isinstance(dict_pessoa, dict)
