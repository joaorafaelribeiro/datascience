from database.dao import DAO

class Repository:
    _dao = None

    def __init__(self) :
        self._dao = DAO()

    def obterOrgaosUnidade(self):
        ous = self._dao.execute("""
                                 select 
                                    o.idOrgaoUnidade,
                                    dsOrgaoUnidade,
                                    dsTpOu,
                                    NmMunicipio,
                                    dsTpRegional,
                                    en.DsEndereco,
                                    b.NmBairro,
                                    en.NuCEP
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
                                 """)
        ous.columns = ['Id','Nome','Tipo','Município','Região','Endereço','Bairro','CEP']
        return ous
    
    def obterTotalProcessos(self, **ids):
        processos = self._dao.execute(f"""
                                    select 
                                        p.IdOrgaoUnidade, 
                                        count(p.Idprocesso) as NuTotal 
                                    from 
                                        tProcesso p 
                                    where 
                                        p.IdOrgaoUnidade in ({0})
                                    group by p.IdOrgaoUnidade
                                      """.format(ids))
        processos.columns = ['Id', 'Total']
        return processos
    
    def obterTotalMovimentacoes(self, **ids):
        movimentacoes = self._dao.execute(f"""
                                         select 
                                            p.IdOrgaoUnidadeResponsavel, 
                                            count(p.IdProcMov) as NuTotal 
                                        from 
                                            tProcMov p 
                                        where 
                                            p.IdOrgaoUnidadeResponsavel in ({0})
                                        group by p.IdOrgaoUnidadeResponsavel              
                                          """.format(ids))
        movimentacoes.columns = ['Id', 'Total']
        return movimentacoes