import unittest
from util.geo_cep import location

    
def test_get_location_by_cep():
    local = location("41620430")
    assert local != None, 'endereço não encontrado'