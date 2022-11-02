import streamlit as st
from streamlit_folium import st_folium
import folium
import database.database as db

bahia = (-11.409874, -41.280857)
coords = db.obterCoords()

def obterMarkers():
    return [ folium.Marker(
        [coords['Latitude'][i],coords['Longitude'][i]],
        popup='<h4>Unidades:</h4><hr/>'+coords['Endereco'][i],
        ) for i in coords.index]
        

def map(points: list) -> None:
    with st.container():
        st.header('Localização')
        m = folium.Map(location=bahia, zoom_start=6,no_touch=True)
        for c in obterMarkers():
            c.add_to(m)
        st_folium(m, width = 725)