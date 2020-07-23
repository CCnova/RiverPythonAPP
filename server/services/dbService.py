from mysql.connector import MySQLConnection, Error
from config.mysql_dbconfig import read_db_config 

def connect():
    """ Conecta ao banco de dados MySQL """
    conn = None
    try:
        dbConfig = read_db_config() # Le as configuracoes do banco de dados
        conn = MySQLConnection(**dbConfig) # Realiza a conexao com o banco
        if conn.is_connected():
            print('Conexao com Banco de dados {} feita com sucesso'.format(dbConfig['database']))

        cursor = conn.cursor()
    
    except Error as e:
        print(e)

    finally:
        return [conn, cursor, Error]

def disconnect(dbConnection=None, dbCursor=None):
    if dbConnection is not None and dbConnection.is_connected():
        dbConnection.close()
        dbCursor.close()
        print('Conexao com o banco finalizada!')
