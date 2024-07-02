# Definindo uma classe e palavra reservada self
class PessoaFisica:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
        
    # Estudar isso aqui, pq parece com método de extensão de C#
    @classmethod
    def criar_sem_nome(cls, idade): # cls equivale a this
        return cls('Anônimo', idade)
    
    # Propriedades de uma classe
    @property # Equivalente ao get
    def nome(self):
        return self._nome
    
    @nome.setter # Equivalente ao set
    def nome(self, value):
        self._nome = value

        
p3 = PessoaFisica.criar_sem_nome(28)
p1 = PessoaFisica('Wanderley Ferreira', 34)
p2 = PessoaFisica('Sthéfannie Santos', 32)

# Dicionário interno dos atributos da classe
atributos = p1.__dict__
atributos = vars(p1)

p1.nome = 'Tiririca'
print(p1.nome)

# HERANÇA
print(help(PessoaFisica))
class Pessoa: ...
class Cliente(Pessoa, PessoaFisica): ...
class Aluno(Pessoa): ...

# Sobrescrita parcial
class MinhaString(str):
    def upper(self):
        print("Aqui mexo em tudo")
        return super().upper()
