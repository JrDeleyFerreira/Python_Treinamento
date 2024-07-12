import subprocess
import sys

plataforma = sys.platform # Qual o SO
cmd = ['ping', '127.0.0.1', '-c', '4'] # Comando no cmd Linux/Mac
encoding_default = 'utf8'

if plataforma == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding_default = 'cp850'

proc_ping = subprocess.run(cmd) # Aciona o processo

print(f'{proc_ping} \n') # Print do resultado do processo
print(proc_ping.args) # Argumentos
print(proc_ping.stdout) # Saída
print(proc_ping.stderr) # Erros
print(f'{proc_ping.returncode} \n') # Código do erro

proc_ping_2 = subprocess.run(cmd, capture_output= True)
print(proc_ping_2.stdout.decode(encoding= encoding_default)) # Saída definindo o encoding

proc_ping_3 = subprocess.run(cmd, capture_output= True, text= True)
print(proc_ping_3.stdout) # Saída com text=True já define o encoding padrão do sistema

