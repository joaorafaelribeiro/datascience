import pydoc
import os
from typing import str, list

class SqlServer:

    _server: str = ''
    _database: str = ''
    _username: str = ''
    _password: str = ''
    _connect = None
    __instance = None

    def __init__(self):
        if  SqlServer.__instance != None:
            raise Exception('Use GetInstance method static to instance this class')
        self._database = os.environ.get('SQL_SERVER_DATABASE') or 'IDEA'
        self._server = os.environ.get('SQL_SERVER_HOST') or 'KAAN\desenvolvimento'
        self._password = os.environ.get('SQL_SERVER_PASSWORD') or 'useridea'
        self._username =  os.environ.get('SQL_SERVER_USERNAME') or 'IDEA'
        self._connect = pydoc.connect(f"Drive={{SQL Server Native Client 11.0}};Server={self._server};Database={self._database};UID={self._username};PWD={self._password}")
        SqlServer.__instance = self
        assert self._connect != None

    @staticmethod
    def GetInstance():
        if SqlServer.__instance == None:
            SqlServer()
        return SqlServer.__instance

    def execute(self,sql: str) -> list:
        return self._connect.cursor().execute(sql).fetchone()
