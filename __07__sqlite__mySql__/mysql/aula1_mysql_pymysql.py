import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host= 'localhost',
    database= 'db_mysql',
    user= 'usuario',
    password= 'senha',
    charset= 'utf8mb4',
    # cursorclass= pymysql.cursors.DictCursor,
    # Usam menos memória na leitura, pois usa o método .scroll()
    # cursorclass= pymysql.cursors.SSCursor, 
    cursorclass= pymysql.cursors.SSDictCursor
)

with connection:
    with connection.cursor() as cursor: # Create simples
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR2(50) NOT NULL, '
            'age INT NOT NULL) ,'
            'PRIMARY KEY (id))'
        )
        
    with connection.cursor() as cursor: # Insert com parâmetros
        sql = f'INSERT INTO {TABLE_NAME} values (%s, %s, %s)'
        cursor.execute(sql, (None, 'Wanderley', 34))
        
    with connection.cursor() as cursor: # Insert com dicionário
        data = {'id': None, 'name': 'Isabelle', 'age': 3}
        sql2 = f'INSERT INTO {TABLE_NAME} values (%(id)s, %(name)s, %(age)s)'
        cursor.execute(sql2, data)
        
    with connection.cursor() as cursor: # Insert de vários registros
        data2 = (
            (None, 'Rafael', 28),
            (None, 'Cíntia', 35),
            (None, 'Márcia', 58)
        )
        sql3 = f'INSERT INTO {TABLE_NAME} values (%(id)s, %(name)s, %(age)s)'
        cursor.executemany(sql3, data2)
        
    with connection.cursor() as cursor: # Select - Cursor retornando dict()
        sql4 = f'SELECT * FROM {TABLE_NAME} where id = (%s)'
        cursor.execute(sql4, 4)
        for row in cursor.fetchall():
            print(row)
    # Basta adicionar cursorclass= pymysql.cursors.DictCursor na criação da conexão
    
    with connection.cursor() as cursor: # Select intermediário com scroll()
        sql5 = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(sql5)
        for row in cursor.fetchall_unbuffered():
            print(row)
        cursor.scroll(-2, 'absolute')
        for row in cursor.fetchall_unbuffered():
            print(row)
    
    with connection.cursor() as cursor: # Select - Cursor sem buffer de memória retornando dict()
        sql6 = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(sql6)
        for row in cursor.fetchall_unbuffered():
            print(row)
            if row['id'] > 5:
                break
        for row in cursor.fetchall_unbuffered():
            print(row)
    
    connection.commit()