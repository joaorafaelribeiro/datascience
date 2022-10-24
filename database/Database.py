import SqlServer

class Database:
    
    _database = None

    def __init__(self) -> None:
        self._database = SqlServer.GetInstance()

    def GetAtividades(self):
        return self._database.execute('select * from tAtividadesRAF')