import database.create_schema as db

def test_create_tables():
    db.create_tables()
    assert db.exists('tOrgaoUnidades')
    assert db.exists('tProcessos')
    assert db.exists('tClasses')
    assert db.exists('tMovimentos')
    assert db.exists('tAnalise')
    assert db.exists('tClassesOrgaoUnidade')
    
#def test_feed():
#    assert db.feeds() > 0
