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
def imprimir_2(a: int, b: int, c: int): ... # Parâmetros dinâmicos
def imprimir_3(a: int = 80): ... # Com valor default

def imprime_frase():
    frase = 'Simples assim'
    return frase

final = imprime_frase()
print(final)

# Problemas com parâmetros mutáveis

# Nunca faça assim, iniciando a variável de parâmetro
def adiciona_pessoa(nome, lista =[]):
    ...

# Dessa forma, vc é obrigado a passar uma lista
def lista_tipada(nome: str, lista: list[str]):
    lista.append(nome)
    return lista

# Dessa forma, 
def adiciona_pessoa(nome: str, lista: list[str] | None = None) -> list[str] | None:
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_pessoa('Wanderley')
adiciona_pessoa('Edu', cliente1)
print(cliente1)

cliente2 = adiciona_pessoa('Fernanda')
adiciona_pessoa('Sthéfannie', cliente2)
print(cliente2)