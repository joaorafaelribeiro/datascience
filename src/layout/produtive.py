import streamlit as st
import pandas as pd
import numpy as np

def produtive():
    with st.container():
        st.header('Produtividade')
        chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['Processos', 'Movimentações'])
        st.line_chart(chart_data)