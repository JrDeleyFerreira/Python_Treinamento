import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent
BASE = 'db_sqlite.sqlite3'
DB_FILE = ROOT_PATH / BASE

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Create - Insert - Update - Delete - Read
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'name TEXT, '
        'weight REAL)'
    )

connection.commit() # Commit de segurança da criação

# Evita sql injection
insert_bindings = f'INSERT INTO {TABLE_NAME} values (?, ?, ?)'
cursor.execute(insert_bindings, (None, 'Wanderley', 70.3))

# Inserindo diversos - Qnd for apenas 1, podemos usar o cursor.execute()
cursor.executemany(
    insert_bindings,
    ((None, 'Márcia', 72), (None, 'Rafael', 103), (None, 'Isabelle', 16.4))
) # Tuplas são mais performáticas nesse caso

connection.commit()

if __name__ == '__main__':
    cursor.close()
    connection.close()
