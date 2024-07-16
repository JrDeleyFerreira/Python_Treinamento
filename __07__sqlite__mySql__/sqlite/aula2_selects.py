import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent
BASE = 'db_sqlite.sqlite3'
DB_FILE = ROOT_PATH / BASE

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

command_select = f'SELECT * FROM {TABLE_NAME}'
cursor.execute(command_select)
for row in cursor.fetchall():
    _id, _nome, _peso = row
    print(_id, _nome, _peso)

cursor.close()
connection.close()