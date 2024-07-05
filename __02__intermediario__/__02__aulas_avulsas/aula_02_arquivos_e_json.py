import os
import json
from typing import TypedDict

# Manipulação de arquivos
caminho = 'C:\\Users\\wanderley_junior'
caminho += 'arquivo.txt'
with open(caminho, 'w+') as arquivo:
    pass

os.rename(caminho, 'novo_nome.txt')
os.remove(caminho)
os.unlink(caminho)

# JSON
pessoa = {
    'nome' : 'Wanderley D. Ferreira Júnior',
    'enderecos' : [
        {'rua' : 'Silvio Felicio', 'numero' : 91},
        {'rua' : 'Romana', 'numero' : 188},
    ],
    'idade' : 34,
    'numeros_preferidos' : (5, 11, 14, 17, 30),
    'dev' : True,
    'nada' : None
}

# Salva um objeto em JSON - Normalmente um dict() ou classe do tipo Entity
with open('modelo.json', 'w', encoding='utf8') as arquivo_json:
    json.dump(
        pessoa, # dict() ou classe Entity
        arquivo_json, # Caminho onde será salvo
        ensure_ascii= False, # Mantém acentos e caracter especial
        indent=2 # Faz a identação do json
    )
    
class Pessoa(TypedDict):
    nome: str
    enderecos: list[dict]
    idade: int
    numeros_preferidos: tuple
    dev: bool
    nada: None
    
# Lendo um JSON e salvando numa variável do tipo dict()
with open('modelo.json', 'r', encoding='utf8') as pessoa_leitura:
    nova_pessoa: Pessoa = json.load(pessoa_leitura)
    nova_pessoa['dev']
