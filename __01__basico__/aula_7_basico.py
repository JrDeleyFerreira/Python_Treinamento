# Lista é um objeto iterável
lista = [n for n in range(1000)]
iterator = lista.__iter__()
iterator = iter(lista)
# Teria que printar 1000x para ver tds os resultados
print(next(iterator))

# Generator
generator = (n for n in range(1000))
print(next(generator))

for valor in generator:
    pass # Pode criar qualquer lógica para cada elemeto

# Generator Functions
def func_generator(n=0):
    yield True if n % 2 == 0 else False
    print(f'O número digitado foi: {n}')
    yield n + 10
    print(f'{n} + 10 = {n + 10}')
    return print('ACABOU')
    
gen = func_generator(4)
print(next(gen)) # Pega o resultado do 1º yield
print(next(gen)) # Pega o 1º print e o 2º yield
print(next(gen)) # Levanta exceção pq acabou

for pause in gen: # Não levanta exceção
    print(pause)
