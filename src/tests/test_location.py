import pytest
from util.geo_cep import location
import database.idea as idea

def test_obter_coord_by_cep():
    assert location("LARGO DA INDEPENDÊNCIA, Kennedy, Alagoinhas BA") != None, 'endereço não encontrado'