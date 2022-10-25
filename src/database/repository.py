from connect import Connect
from model.info import Info

class Repository:
    _con = None

    def __init__(self) -> None:
        self._con = Connect.GetConnect()

    def ObterInfo(self, id = None):
        info = Info()
        info.orgaos = self._con('select * from ')
        return info
