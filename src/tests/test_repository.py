import unittest
from database.repository import Repository

    
def test_obter_orgaos_unidades():
        rep = Repository()
        result = rep.obterOrgaosUnidade()
        assert result.empty == False, 'O metodo Repository.obterOrgaosUnidade() retornou vazio'
        
def test_obter_cep_orgaos_unidades():
        rep = Repository()
        result = rep.obterOrgaosUnidade()
        ceps = result['CEP'].unique()
        assert len(ceps) > 0, "não carregou os CEPs"