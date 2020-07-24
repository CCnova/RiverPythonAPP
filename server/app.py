from services import dbService, amostraService
import datetime
from models.amostra import Amostra

def insertAmostra():
    id_amostra = input('Digite um numero identificador da Amostra:\n')
    data = input('Digite a data que a Amostra foi coletada: dd/mm/yy\n') 
    id_amostrador = input('Digite o id do amostrador\n')
    id_ponto = input('Digite o id do Ponto:\n')
    id_campanha = input('Digite o id da campanha\n')
    id_equipamento = input('Digite o id do equipamento\n')
    id_projeto = input('Digite o id do projeto\n')
    novaAmostra = Amostra(id_amostra, data, id_amostrador, id_ponto, id_campanha, id_equipamento, id_projeto)
    print('''Dados digitados da Amostra:\n
             Data: {}\n
             Amostrador: {}\n
             Campanha: {}\n
             Equipamento: {}\n
             Projeto: {}\n'''.format(novaAmostra.data, novaAmostra.idAmostrador, novaAmostra.idCampanha, novaAmostra.idEquipamento, novaAmostra.idProjeto))
    
    amostraService.insert(novaAmostra)


def runApp():
    insertAmostra()

if __name__ == '__main__':
    runApp()