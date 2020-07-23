""" 
    Modulo que le a configuracao do banco de dados 
    do arquivo de configuracao 'config.ini' e retorna
    um dicionario 
"""

from configparser import ConfigParser

def read_db_config(filename='./config/config.ini', section='mysql'):
    """
    :param filename: nome do arquivo de configuracao
    :param section: secao da configuracao do banco de dados
    :return: Dicionario com os parametros do banco de dados
    """

    # Cria parser e le o arquivo de configuracao
    parser = ConfigParser()
    parser.read(filename)

    print('Nome do arquivo de configuracao: {}'.format(filename))
    print('O arquivo possui secao {}: {}'.format(section, parser.has_section(section)))

    # Le a secao
    db = {}
    if parser.has_section(section): # Checa se o arquivo possui a secao fornecida
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1] # Semea o dicionario
    else:
        raise Exception('{} not found in the {} file'.format(section, filename))

    return db