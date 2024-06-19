# Desempacotamento
_, valor1, valor2, *_ = ['Piracanjuba', 'Chamito', 'Itambé', 'Italac', 'Piaçu']
print(valor1)
print(valor2)
print(_)

# Tuplas
nomes = ()
idades = (12, 18, 26)
reais = 25.6, 29.9, 30.45

for indice, valor in enumerate(reais):
    print(f'{indice} - {valor}')
    
# Funções
def imprimir(a: int, b: str, c: int): ... # Parâmetros tipados
def imprimir_2(a, b, c): ... # Parâmetros dinâmicos
def imprimir_3(a= 80): ... # Com valor default

def imprime_frase():
    frase = 'Simples assim'
    return frase

final = imprime_frase()
print(final)