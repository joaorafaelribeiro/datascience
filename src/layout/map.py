import streamlit as st
from streamlit_folium import st_folium
import folium

bahia = (-11.409874, -41.280857)

def map(points: list) -> None:
    with st.container():
        st.header('Localização')
        m = folium.Map(location=bahia, zoom_start=6)
        st_folium(m, width = 725)