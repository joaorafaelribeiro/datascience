import pyodbc
import os

class Connect:
    
    _instance = None
    _user: str = None
    _password: str = None
    _server: str = None
    _database: str  = None
    _connection = None
    _strconnection: str = None
    _drive: str = None
    @staticmethod
    def getInstance():
        if Connect._instance == None:
            Connect()
        return Connect._instance

    def __init__(self) -> None:
        if Connect._instance != None:
            raise Exception("use GetConnect static method")
        Connect._instance = self
        self._user = os.environ.get('DATABASE_USER') or  'idea'
        self._password = os.environ.get('DATABASE_PWD') or 'useridea'
        self._database = os.environ.get('DATABASE_NANE') or 'idea'
        self._server = os.environ.get('DATABASE_SERVER') or 'kaan\homologacao'
        self._drive = os.environ.get('ODBC_DRIVE') or 'SQL Server'
        self._strconnection = "Driver={"+self._drive+"};SERVER="+self._server+";Database="+self._database+";UID="+self._user+";PWD="+self._password+";"
        self._connection = pyodbc.connect(self._strconnection).cursor()

    

    def execute(self, str):
        print(self._connection)
        return self._connection.execute(str).fetchall()
    
    def __str__(self) -> str:
        return self._strconnection