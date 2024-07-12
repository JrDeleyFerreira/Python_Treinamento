import requests
from bs4 import BeautifulSoup

url_base = 'http://localhost:3333'

response = requests.get(url= url_base)

print(response.status_code) # Status
# print(response.headers) # Cabeçalho
# print(response.content) # Conteúdo em forma de bytes
# print(response.text) # Conteúdo em forma de texto
# print(response.json()) # Conteúdo em forma de JSON, caso a API devolva nesse formato

# Transforma todo o conteúdo de texto em objetos Python
parse_html = BeautifulSoup(response.text, 'html.parser')

# Deve verificar pq o framework retorna Tag | None
if parse_html.title is not None: # title não é um snippets padrão
    print(parse_html.title.text)

top_jobs_heading = parse_html.select_one('#into > div > div > article > h2')
if top_jobs_heading is not None:
# Pega o título do artigo
    print(top_jobs_heading.text)
# Pega todos os parágrafos do artigo
    article = top_jobs_heading.parent
    if article is not None:
        for paragraph in article.select('p'):
            print(paragraph)
