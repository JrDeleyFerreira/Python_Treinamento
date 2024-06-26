# from textblob import TextBlob
# https://www.youtube.com/watch?v=Wx3SyNwZtsA

def gera_funcao(funcao, x):
    def interna_pause(y):
        return funcao(x, y)
    return interna_pause

def soma(x, y):
    return x + y

def mutiplica(x, y):
    return x * y
    
soma_com_5 = gera_funcao(soma, 5)
print(soma_com_5(8))

mutiplica_por_3 = gera_funcao(mutiplica, 3)
print(mutiplica_por_3(4))

# Variável nonlocal
valor_final = 'Inicio de tudo' # global
def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    
    return interna

c = concatenar('')
print(c('a'))
print(c('e'))
print(c('i'))
print(c('o'))
print(c('u'))
print('\n \n')

# frase = 'O mai pior foi o diia em que o monino firiu a perna na cerca de arame farpudo.'
# texto_formatado = TextBlob(frase)

# print(texto_formatado.correct())