# Tratamento de exceções
try: pass
except StopIteration as error: ...
finally: ...
    
# ID na memória
vinculo = ''
print(id(vinculo))

contador = 0
contador += 1 # Incremento - Não aceita ++

# Laços de repetição
for letra in vinculo:
    ...    
for numero in range(12, 48, 4):
    pass

# Equals com dunder function (2 underlines)
if vinculo.__eq__(""):
    print('String vazia!')

# Listas
lista1 = list() # Notação de lista
lista2 = [] # Mais usado
lista3 = [123, True, 'Wanderley', 4.5, []] # Iniciada e dinâmica

print(type(lista3))
print(bool(lista1), bool(lista2)) # Verifica se é vazia
print(lista3)

del lista3[1]
print(lista3)

lista1 = lista3.copy()
lista1.append('Valor add apenas na cópia')
print(lista1)

lista3.clear()
print(lista3)

# Lis Comprehension
lista_range = [numero * 2 for numero in range(15)]
print(f'\n {lista_range}')
