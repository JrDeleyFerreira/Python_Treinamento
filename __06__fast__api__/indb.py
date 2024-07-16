from products import Products
import json
from pathlib import Path

RAIZ = Path(__file__)
DIRETORIO = RAIZ.parent  / 'data/products.json'

def load_products():
    with open(DIRETORIO, 'r', encoding= 'utf-8') as arquivo:
        # data = json.loads(arquivo.read())
        data: Products = json.load(arquivo)
        return data