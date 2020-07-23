from services import dbService
import datetime

def runApp():
    dbObjects = dbService.connect()
    id_amostra = input('Digite um numero identificador da Amostra:\n')
    data = input('Digite a data que a Amostra foi coletada: dd/mm/yy\n') 
    id_amostrador = input('Digite o id do amostrador\n')
    id_ponto = input('Digite o id do Ponto:\n')
    id_campanha = input('Digite o id da campanha\n')
    id_equipamento = input('Digite o id do equipamento\n')
    id_projeto = input('Digite o id do projeto\n')
    print('''Dados digitados da Amostra:\n
             Data: {}\n
             Amostrador: {}\n
             Campanha: {}\n
             Equipamento: {}\n
             Projeto: {}\n'''.format(data, id_amostrador, id_campanha, id_equipamento, id_projeto))

    try:
        dbObjects[1].execute("INSERT INTO `projeto_pibic`.`Amostra` (`id_amostra`, `data`, `id_amostrador`, `id_ponto`, `id_campanha`, `id_equipamento`, `id_projeto`) VALUES ({}, {}, {}, {}, {}, {}, {});".format(id_amostra, data, id_amostrador, id_ponto, id_campanha, id_equipamento, id_projeto))
        print('Amostra inserida com sucesso!')

    except dbObjects[2] as e:
        print(e)


if __name__ == '__main__':
    runApp()