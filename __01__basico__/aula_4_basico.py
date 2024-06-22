# Escopo de variáveis
numero = 1

def imprime_dobro():
    numero = 10  
    def imprime_metade():
        global numero
        numero = 22
        print(numero / 2)       
    imprime_metade()
    print(numero * 2)

print(numero)
imprime_dobro()
print(numero)

# Função com retorno e tipagem de retorno
def soma(*args):
    return sum(args)

_, _, *args = 1, 1, 2, 3, 4, 5 # Desempacotamento
somatorio = soma(*args)
print(somatorio) # resultado = 14

# Higher Order Functions - Funções de primeira classe
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): # *args recebe tudo após a função
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))

# Closure - Funções que podem retornar outras funções como resultado
def criar_saudacao(mensagem):
    def saudar(nome):
        return f'{mensagem}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia')
print(s1('Wanderley'))

