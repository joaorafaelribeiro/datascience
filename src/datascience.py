import streamlit as st
from layout.breadcrumbs import breadcrumbs
st.set_page_config(
    page_title='Ministério Público do Estado da Bahia',
    page_icon=":bank:",
    layout="centered",
    menu_items=None
)
breadcrumbs('')
c = st.container()

c.title('Análise de Dados - Ministério Público do Estado da Bahia')