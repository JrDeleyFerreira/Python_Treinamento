from datetime import datetime, timedelta
from pytz import timezone
import calendar
import locale

# Criação de data
data = datetime(2024, 7, 2)

# Conversão de uma string em data
data_string = '2024-02-11 07:45:22'
data_convert = datetime.strptime(data_string, '%Y-%m-%d %H:%M:%S')
format_data_convert = data_convert.strftime('%d/%m-%Y | %H:%M')
print(format_data_convert)

# Conversão de uma data em string
string_data = str(data)

# Data atual do sistema
data_hoje = datetime.now()

# Data atual em outro país com timezone()
data_hj_tokyo = datetime.now(timezone('Asia/Tokyo'))

# Criar data com timezone()
data_criada = datetime(2024, 7, 2, 18, 25, 16, tzinfo=timezone('Asia/Tokyo'))

# Timestamp() e fromtimestamp() - Converte em segundos e recria a data a partir dos segundos
time_segundos = data_convert.timestamp()
recria_ttmp = datetime.fromtimestamp(time_segundos)

# Operações com datas:
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

print(data_inicio > data_fim) # Comparações >, <, ==, >= e <=

delta_op = data_fim - data_inicio # Delta obtido por operação (-)
print(f'Dias: {delta_op.days} - Total Sec.: {delta_op.total_seconds()}')

delta = timedelta(days= delta_op.days, hours=2) # Delta gerado para operações

print(data_fim + delta) # Se usar delta_op no lugar de delta, dá erro

# Calendário
print(calendar.calendar(2024)) # Imprime o calendário do ano
print(calendar.month(2024, 7)) # Imprime o calendário do mês, naquele ano
print(calendar.monthrange(2024, 5)) # Imprime o índice do dia da semana e último dia do mês
print(list(calendar.month_name)) # Lista de nomes dos meses
print(list(enumerate(calendar.day_name))) # Lista os nomes dos dias da semana

# Localização
print(f'Get = {locale.getlocale()} || GetEncoding = {locale.getencoding()}')
locale.setlocale(locale.LC_ALL, '')
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
