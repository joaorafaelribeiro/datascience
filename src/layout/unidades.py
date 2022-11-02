import streamlit as st
import database.database as db

unidades = db.Unidades().get()

def table():
    st.header('Órgãos/Unidades')
    st.dataframe(unidades)