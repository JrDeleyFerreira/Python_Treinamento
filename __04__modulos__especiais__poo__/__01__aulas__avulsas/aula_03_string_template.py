import string
import locale
from datetime import datetime

texto_padrao = """Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia ${data}. Caso deseje cancelar o serviço, entre em contato com a ${empresa} pelo telefone ${telefone}.

Atenciosamente,

${empresa}, """

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

template = string.Template(texto_padrao)
print(template.substitute(dados)) # Se faltar 1 variável, dá erro
print(template.safe_substitute(dados)) # Se faltar 1 variável, apenas deixa sem preencher

