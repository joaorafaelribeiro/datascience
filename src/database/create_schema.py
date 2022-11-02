import sqlite3
import database.idea as idea
from util.geo_cep import location
import database.database as db

con = sqlite3.connect('datascience.db')
cursor = con.cursor()

def create_tables():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS tOrgaoUnidades(
                    Id integer primary key,
                    Nome text,
                    Tipo text,
                    Municipio text,
                    Regional text,
                    Endereco text,
                    Bairro text,
                    CEP text,
                    Latitude real,
                    Longitude real);""")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS tAnalise (
                    Data integer not null,
                    Tipo integer not null default 0,
                    Media number not null default 0,
                    Moda number not null default 0,
                    DesvioPadrao number not null default 0,
                    primary key (Data, Tipo)
                    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tProcessos (
                    Data integer not null,
                    IdOrgaoUnidade integer references tOrgaoUnidades(IdOrgaoUnidade),
                    NuTotal integer not null default 0,
                    primary key (Data, IdOrgaoUnidade))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tMovimentos (
                    Data integer not null,
                    IdOrgaoUnidade integer references tOrgaoUnidades(IdOrgaoUnidade),
                    NuTotal integer not null default 0,
                    primary key (Data, IdOrgaoUnidade))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tClasses (
                    Id integer primary key,
                    Nome text,
                    IdClassePai integer references tClasses(IdClasse))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tClassesOrgaoUnidade (
                    Data integer,
                    IdOrgaoUnidade integer references tOrgaoUnidades(IdOrgaoUnidade),
                    IdClasse integer references tClasses(IdClasse),
                    NuTotal integer not null default 0,
                    primary key (Data, IdOrgaoUnidade, IdClasse))""")

def exists(table):
    has = cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table' AND tbl_name='{table}'").fetchall()
    return len(has) != 0
 
def feeds():
    rep = IDEA()
    db.insertOrgaoUnidades(rep.obterOrgaosUnidade())
    db.insertClasses(rep.obterClasses())
    db.updateCoords()
    return db.count('tOrgaoUnidades') + db.count('tClasses')
