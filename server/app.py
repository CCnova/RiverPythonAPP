from services import dbService

def runApp():
    dbService.connect()


if __name__ == '__main__':
    runApp()