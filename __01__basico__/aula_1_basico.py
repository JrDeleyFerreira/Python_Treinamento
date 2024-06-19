# Variáveis dinâmicas:
meu_nome = "Wanderley"
minha_idade = 34
meu_peso = 71.7

# Prints com interpolação e tipagem dos dados
print(f'Nome: {meu_nome} - Idade: {minha_idade} - Peso: {meu_peso}')
print(f'Nome: {type(meu_nome)} - Idade: {type(minha_idade)} - Peso: {type(meu_peso)}')

# As letras após o símbolo de % indicam:
# s -> str
# d e i -> int
# f -> float
# x e X -> Hexadecimal
interpolacao = '%s, a altura é: R$ %.2f' % (meu_nome, meu_peso)
print(interpolacao)

# string.format()
format_string = '{0} {1} {2} - {0}'
texto_final = format_string.format(meu_nome, minha_idade, meu_peso)
print(texto_final)

# Pré-definição de variáveis - Utilizado em Entity
local: str = 'Lista de desejos'
numero: int = 78
latitude: float = 7.28
luz_acesa: bool = True
var_Any: None

print(type(local), local)

# Assim q se faz um comentário
'''
Assim posso colocar informações, porém, não é um comentário,
mas sim uma informação q fica na memória
'''
# Imprime o nameof() e o valor da variável
primeiro_valor = 25
print(f'{primeiro_valor=}')

if not luz_acesa:
    print('APAGADA')
else:
    print("ACESA")
    
# Tamanho
print(len(local))