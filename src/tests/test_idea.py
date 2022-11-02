import database.idea as idea
        
def test_IDEA_orgaosunidade():
        assert idea.orgaosunidade().empty == False, 'orgaosunidade vazio'
        
def test_IDEA_classes():
        ids = idea.orgaosunidade()['Id']
        assert idea.classes(ids).empty == False, 'classes vazio'
        
def test_IDEA_processos():
        ids = idea.orgaosunidade()['Id']
        assert idea.processos(ids).empty == False, 'processos vazio'

def test_IDEA_movimentos():
        ids = idea.orgaosunidade()['Id']
        assert idea.movimentos(ids).empty == False, 'movimentos vazio'
        
def test_IDEA_resumo():
        resumo = idea.resumo()
        assert resumo != None, 'resumo vazio'
        assert resumo.data != None, 'resumo.data vazio'
        assert resumo.processos.empty == False, 'resumo.processo vazio'
        assert resumo.movimentos.empty == False, 'resumo.movimentos vazio'
        assert resumo.classes.empty == False, 'resumo.classes vazio'