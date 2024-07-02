class DunderM:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
    
    def __str__(self):
        pass
    
    def __repr__(self) -> str:
        return f'x = {self._x!r} | y = {self._y}'
    
p1 = DunderM(18, 'Seringa')
print(repr(p1))
# --------------------------------------------------
# Classes decoradas com funções

def meu_repr(self): # __repr__ padronizado
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr # Atribui o __repr__ padronizado
    return cls

@adiciona_repr # Decoração q evita herança
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr # Decoração q evita herança
class Planeta:
    def __init__(self, nome):
        self.nome = nome

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

# --------------------------------------------------
# Funções decoradas com classes
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func): # func aqui é soma()
        def interna(*args, **kwargs): # *args recebe oq foi passado na linha 66
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(2) # O parâmetro é o multiplicador
def soma(x, y): 
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)