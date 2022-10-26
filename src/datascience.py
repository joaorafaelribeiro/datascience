import streamlit as st
from database.repository import Repository
from layout.breadcrumbs import breadcrumbs
from layout.map import map
from layout.produtive import produtive
from layout.categories import categories



st.set_page_config(
    page_title='Ministério Público do Estado da Bahia',
    page_icon=":bank:",
    layout="centered",
    menu_items=None
)
st.title('Análise de Dados - Ministério Público do Estado da Bahia')

with st.container():
    map(None)
    produtive()
    categories()
    
#st.table(repo.obterOrgaosUnidade())