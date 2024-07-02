import metaclasses
import enum
# from enum import Enum

print(dir(metaclasses))
help(metaclasses)

# --------- ENUM ---------
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class DirecoesEnum(enum.Enum):
    ESQUERDA = 1, # Onde está o 1, pode ser uma str
    DIREITA = enum.auto() # Gera sequência automática
    
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