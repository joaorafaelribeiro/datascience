import database.database as db
import database.idea as idea
import pandas as pd
from datetime import date

def test_DATABASE_orgaosunidade():
    assert isinstance(db.Unidades().get(), pd.DataFrame)

def test_DATABASE_processos():
    assert isinstance(db.Processos().get(date.today()), pd.DataFrame)

def test_DATABASE_movimentos():
    assert isinstance(db.Movimentos().get(date.today()), pd.DataFrame)
    
def test_DATABASE_classes():
    assert isinstance(db.Classes().get(), pd.DataFrame)