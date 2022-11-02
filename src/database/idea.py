import pyodbc
import pandas as pd
import os
from datetime import date
import util.log as log
from model.resumo import Resumo


user = os.environ.get('DATABASE_USER') or  'idea'
password = os.environ.get('DATABASE_PWD') or 'useridea'
database = os.environ.get('DATABASE_NANE') or 'idea'
server = os.environ.get('DATABASE_SERVER') or 'kaan\homologacao'
drive = os.environ.get('ODBC_DRIVE') or 'SQL Server'
strconnection = f"Driver={{SQL Server}};SERVER={server};Database={database};UID={user};PWD={password};"
con = pyodbc.connect(strconnection)

def orgaosunidade():
    log.info('consultar unidades')
    return pd.read_sql("""
                            select 
                            o.idOrgaoUnidade as Id,
                            dsOrgaoUnidade as Nome,
                            dsTpOu as Tipo,
                            NmMunicipio as Municipio,
                            dsTpRegional as Regional,
                            en.DsEndereco as Endereco,
                            b.NmBairro as Bairro,
                            en.NuCEP as CEP,
                            0 as Latitude,
                            0 as Longitude
                        from 
                            vw_from_OU_DS01_OrgaoUnidadeTodos o
                            left join vw_from_OU_DS21_EnderecoOUAssocia ends on ends.IdOrgaoUnidade = o.IdOrgaoUnidade
                            left join vw_from_OU_DS29_OUEndereco en on en.IdEnderecoOU = ends.IdEnderecoOU
                            left join vw_from_OU_DS10_OUCoordenadaGeo c on c.IdOrgaoUnidade = o.IdOrgaoUnidade
                            inner join vw_from_CORREIO_DS02_Bairro b on b.CdBairro = en.CdBairro 
                        where 
                            o.stAtivo = 1 and 
                            idTpOU in (4,5) and stTpOE = 0 
                            and en.NuCEP is not null
                        order by dsOrgaoUnidade 
                            """, con)
    
def processos(ids):
    assert isinstance(ids, pd.Series)
    log.info('obter total de processos')
    str_ids = ids.astype("string").str.cat(sep=",")
    return pd.read_sql("""
                                select
                                    convert(date,getdate()) as data, 
                                    p.IdOrgaoUnidade as IdOrgaoUnidade, 
                                    count(p.Idprocesso) as NuTotal 
                                from 
                                    tProcesso p 
                                where 
                                    p.IdOrgaoUnidade in ({})
                                group by p.IdOrgaoUnidade
                                    """.format(str_ids), con)
    
def movimentos(ids):
    assert isinstance(ids, pd.Series)
    log.info('obter total de movimentos')
    str_ids = ids.astype("string").str.cat(sep=",")
    return pd.read_sql("""select 
                            convert(date,getdate()) as data,
                            p.IdOrgaoUnidadeResponsavel as IdOrgaoUnidade, 
                            count(p.IdProcMov) as NuTotal 
                        from 
                            tProcMov p 
                        where 
                            p.IdOrgaoUnidadeResponsavel in ({})
                        group by p.IdOrgaoUnidadeResponsavel""".format(str_ids),con)

def classes(ids = None): 
    log.info('obter classes')
    if isinstance(ids, pd.Series):
        return pd.read_sql("select CdItem as Id, NmItem as Nome, CdItemPai as IdClassePai from titem where DsTpItem = 'C' order by NmItem",con)
    str_ids = ids.astype("string").str.cat(sep=",")
    return pd.read_sql("""
                       select 
                            convert(date,getdate()) as data,
                            p.IdOrgaoUnidadeResponsavel as IdOrgaoUnidade,
                            p.CdClasse as Classe,
                            count(p.CdClasse) as NuTotal 
                        from 
                            tProcMov p 
                        where 
                            p.IdOrgaoUnidadeResponsavel in ({})
                        group by p.IdOrgaoUnidadeResponsavel, p.CdClasse
                       """.format(str_ids),con)
def resumo() -> Resumo:
    log.info('criar resumo para analise')
    ids = orgaosunidade()['Id']
    resumo = Resumo()
    resumo.data = date.today()
    resumo.processos = processos(ids)
    resumo.movimentos = movimentos(ids)
    resumo.classes = classes(ids)
    return resumo