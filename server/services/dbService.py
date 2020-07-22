import mysql.connector
from mysql.connector import Error

database_name = 'projeto_pibic'

def connect():
    """ Conecta ao banco de dados MySQL """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database=database_name,
                                       user='root',
                                       password='password')
        if conn.is_connected():
            print('Conexao com Banco de dados {} feita com sucesso'.format(database_name))
    
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

    