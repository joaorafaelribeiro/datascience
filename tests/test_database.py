import unittest

from database import Database

class TestDatabase(unittest.TestCase):
    def TestConnect(self):
        Database()

    def TestGetAtividades(self):
        database = Database()
        atividades = database.GetAtividades()
        self.assertIsNotNone(atividades,"Atividades não é vazio")