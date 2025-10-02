import enum
# from enum import Enum
from enum import IntEnum

# print(dir(metaclasses))
# help(metaclasses)

# --------- ENUM ---------
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class DirecoesEnum(enum.Enum): # Pode ser ReperEnum ou StrEnum
    ESQUERDA = (1, "astolfo"), # Onde está o 1, pode ser uma str
    DIREITA = (2, "braulio") # Gera sequência automática
    
class DirecoesVerticais(IntEnum):
    CIMA = 1
    BAIXO = enum.auto()
    
def mover(direcao: Direcoes | DirecoesEnum):
    if not isinstance(direcao, (Direcoes, DirecoesEnum)):
        raise ValueError('Direção não encontrada!')
    print(f'Movendo para {direcao.name}')
    
mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
print(f'Name: {Direcoes.DIREITA.name} - Value: {Direcoes.DIREITA.value}')
print(f'Name: {Direcoes.ESQUERDA.name} - Value: {Direcoes.ESQUERDA.value}')

print()

mover(DirecoesEnum.DIREITA)
mover(DirecoesEnum.ESQUERDA)
print(f'Name: {DirecoesEnum.DIREITA.name} - Value: {DirecoesEnum.DIREITA.value}')
print(f'Name: {DirecoesEnum.ESQUERDA.name} - Value: {DirecoesEnum.ESQUERDA.value}')