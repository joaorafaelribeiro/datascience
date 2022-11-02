import pandas as pd
import util.geo_cep as geo
import sqlite3
import util.log as log
from model.resumo import Resumo

con = sqlite3.connect('datascience.db', check_same_thread=False)
cursor = con.cursor()

class Unidades:
    def get(self):
        return pd.read_sql_query('select * from tOrgaoUnidades order by Nome',con)
    def save(self, unidades= None):
        unidades.to_sql('tOrgaoUnidades',con,if_exists='append',index=False)
        con.commit()    
    def count(self):
        count('tOrgaosUnidades')
class Classes:
    def get(self):
        return pd.read_sql_query('select * from tClasses',con)
    def save(self, classes=None):
        classes.to_sql('tClasses',con,if_exists='append',index=False)
        con.commit()
    def count(self):
        count('tClasses')
class Processos:
    def get(self, data):        
        return pd.read_sql_query(f'select * from tProcessos where Data = {data}',con)
    def count(self):
        count('tProcessos')
class Movimentos:
    def get(self, data):        
        return pd.read_sql_query(f'select * from tMovimentos where Data = {data}',con)
    def count(self):
        count('tMovimentos')
    
def count(table):
    result = cursor.execute(f"select count(*) from {table}").fetchone()
    log.info(f'total {table} = {result[0]}')
    return result[0]
    
def updateCoords():
    log.info(f'atualizar coords')
    orgaos = obterOrgaosUnidade()
    columns = ['Endereco','Bairro','Municipio','CEP']
    enderecos = orgaos[columns].drop_duplicates(subset=columns)
    for i in enderecos.index:
        rua = enderecos['Endereco'][i]
        bairro = enderecos['Bairro'][i]
        municipio = enderecos['Municipio'][i]
        cep = enderecos['CEP'][i]
        local = geo.location(f"{rua}, {bairro}, {municipio} - Bahia, {cep}")    
        if local:
            con.execute(f'update tOrgaoUnidades set Latitude={local.latitude}, Longitude={local.longitude} where CEP={cep}')
            con.commit()
            
def obterCoords():
    log.info(f'obter coords')
    return pd.read_sql('select distinct Latitude, Longitude, Endereco from tOrgaoUnidades limit 100', con)

def resumo(param):
    assert param != None
    if isinstance(param, Resumo):
        resumo.processos.to_sql('tProcessos',con,if_exists='append',index=False)
        resumo.movimentos.to_sql('tMovimentos',con,if_exists='append',index=False)
        con.commit()
        return cursor.lastrowid
    resumo = Resumo()
    resumo.data = pd.read_sql(f'select * from tAnalise where id = {param}',con)['Data'][0]
    resumo.processos = pd.read_sql(f'select * from tProcessos where idAnalise = {param}',con)
    resumo.movimentos =  pd.read_sql(f'select * from tMovimentos where idAnalise = {param}',con)
    return resumo    