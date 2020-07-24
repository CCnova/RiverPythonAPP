from services import dbService
from models.amostra import Amostra

def insert(amostra):
    dbObjects = dbService.connect() # Objetos do banco {connection, cursor, error}

    print('Tentando inserir amostra...')
    try:
        dbObjects[1].execute("INSERT INTO `projeto_pibic`.`Amostra` (`id_amostra`, `data`, `id_amostrador`, `id_ponto`, `id_campanha`, `id_equipamento`, `id_projeto`) VALUES ({}, {}, {}, {}, {}, {}, {});".format(amostra.id, amostra.data, amostra.idAmostrador, amostra.idPonto, amostra.idCampanha, amostra.idEquipamento, amostra.idProjeto))
        print('Amostra inserida com sucesso!')

    except dbObjects[2] as e:
        print(e)
