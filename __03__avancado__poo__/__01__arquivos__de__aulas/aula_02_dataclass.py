from dataclasses import dataclass, asdict, astuple, field

@dataclass() # @dataclass(frozen=True)
class Pessoa:
    _nome: str
    _sobrenome: str
    _idade: int
    _altura: float = 0.0
    _lista_enderecos: list[str] = field(default_factory=list)
    
    def __post_init__(self):
        self._nome_completo = f'{self._nome} {self._sobrenome}'
    
p1 = Pessoa('Wanderley D', 'Ferreira Jr.', 34)
print(p1._nome)
print(p1._nome_completo)

print(asdict(p1))
print(astuple(p1))

# --------------------------------------------------------
# NamedTuple

from collections import namedtuple
Carta = namedtuple('Carta', ['Valor', 'Naipe'])
as_copas = Carta('A', '❤')

print(as_copas)
print(as_copas.Valor, as_copas.Naipe)


from typing import NamedTuple
class CartaBaralho(NamedTuple):
    valor: str = 'Valor'
    naipe: str = 'Naipe'
    
valete_espada = CartaBaralho('J', '♠')
print(valete_espada)
print(valete_espada.valor, valete_espada.naipe)
