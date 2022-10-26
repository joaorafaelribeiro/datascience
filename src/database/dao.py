import pandas as pn
from database.connect import Connect

class DAO:
    _con = None
    
    def __init__(self) -> None:
        self._con = Connect.getInstance()
        
    def execute(self, sql):
        rows = self._con.execute(sql)
        return pn.DataFrame(tuple(t) for t in rows)