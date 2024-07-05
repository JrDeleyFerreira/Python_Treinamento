from dotenv import load_dotenv
import os

load_dotenv() # Carrega o uso de variáveis de ambiente 

# print(os.environ) # Busca todas as variáveis do Sistema OP

var_usuario = os.getenv('BD_USER')
var_senha = os.getenv('BD_PASSWORD')
var_host = os.getenv('BD_HOST')
var_porta = os.getenv('BD_PORT')

print('Usuário: ', var_usuario)
print('Senha: ', var_senha)
print('Host: ', var_host)
print('Porta: ', var_porta)
