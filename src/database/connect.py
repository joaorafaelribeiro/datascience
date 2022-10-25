import pydoc
import os

class Connect:
    
    _instance = None
    _user = None
    _password = None
    _server = None
    _database  = None
    _connection = None

    def __init__(self) -> None:
        if Connect._instance != None:
            raise Exception("use GetConnect static method")
        Connect._instance = self
        self._user = os.environ.get('DATABASE_USER')
        self._password = os.environ.get('DATABASE_PWD')
        self._database = os.environ.get('DATABASE_NANE')
        self._server = os.environ.get('DATABASE_SERVER')
        self._connection = pydoc.connect(f"Driver={{SQL Server Native Client 11.0}};Server={self._server};Database={self._database};UID={self._user};PWD={self._password};")

    @staticmethod
    def GetConnect(self):
        if Connect._instance == None:
            Connect()
        return Connect._instance

    def execute(self, str):
        return self._connection.execute(str)