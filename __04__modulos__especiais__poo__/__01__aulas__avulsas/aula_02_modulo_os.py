import os
from itertools import count
import shutil

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)

nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
# print(os.path.exists('/Users/luizotavio/Desktop/curso-python-rep'))
print(os.path.abspath('.'))

print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))

if __name__ != '__main__':
# -----------------------------------------------
# Listando diretórios
    caminho2 = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')

    for pasta in os.listdir(caminho2):
        caminho_completo_pasta = os.path.join(caminho2, pasta)
        print(pasta)

        if not os.path.isdir(caminho_completo_pasta):
            continue

        for imagem in os.listdir(caminho_completo_pasta):
            print('  ', imagem)
        
# -----------------------------------------------
# os.walk
    caminho3 = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
    counter = count()

    for root, dirs, files in os.walk(caminho3):
        the_counter = next(counter)
        print(the_counter, 'Pasta atual', root)

        for dir_ in dirs:
            print('  ', the_counter, 'Dir:', dir_)

        for file_ in files:
            caminho_completo_arquivo = os.path.join(root, file_)
            print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
            # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
            # os.unlink(caminho_completo_arquivo)
        
# -----------------------------------------------
# Outros comandos
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
NOVA_PASTA = os.path.join(DESKTOP, 'PASTA_TESTE')

os.makedirs(NOVA_PASTA, exist_ok=True) # Cria uma pasta

# shutil.copyfile() # Copia 1 arquivo
# shutil.copy() # Copia os arquivos e NÃO as subpastas
# shutil.copytree() # Copia tudo
# shutil.rmtree(ignore_errors=True) # Apaga tudo
shutil.move # Aqui falta () e parâmetros, assim como os demais comentados
