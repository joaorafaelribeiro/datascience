import streamlit as st
import database.database as db
from layout.breadcrumbs import breadcrumbs
from layout.map import map
from layout.produtive import produtive
from layout.categories import categories
import layout.unidades as unidades


st.set_page_config(
    page_title='Ministério Público do Estado da Bahia',
    page_icon=":bank:",
    layout="wide",
    menu_items=None
)
st.title('Análise de Dados - Ministério Público do Estado da Bahia')
st.markdown('---')
col1, col2, col3 = st.columns(3)

with col1:
    map(None)
with col2:
    produtive()
    categories()
with col3:
    unidades.table()
    
#st.table(repo.obterOrgaosUnidade())