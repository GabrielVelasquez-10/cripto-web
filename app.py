# region import streamlit dependencies
import streamlit as st
# endregion

# region import global libreries
import pandas as pd
import plotly.graph_objects as go
import time as tm
# endregion

import dataf
from viewf import crypto_cards, graph_candle, graph_line, graph_bar

st.set_page_config(layout="wide")


with st.spinner('Wait for it...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    tm.sleep(0.3)



with st.container(key='cards'): # Cryto cards container
    crypto_cards()

hola = False
with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(key='graphParam'):
            st.write('## Parametros')
            params_selectbox = st.selectbox('Selecciona una criptomoneda', dataf.names_index)
            if hola:
                params_open = st.toggle('Valores de apertura')
                params_close = st.toggle('Valores de Cierre')
            st.write('#### Indicadores')
            params_max = st.checkbox('Max Value')
            params_min = st.checkbox('Min Value')
            params_mean = st.checkbox('Mean Value')
    with col2:
        with st.container(key='graphShow'):
            tab1, tab2, tab3 = st.tabs(['Grafico de Velas', 'Grafico de Lineas', 'Grafico de Barras'])
            with tab1:
                graph_candle(params_selectbox, params_max, params_min, params_mean)
            with tab2:
                graph_line(params_selectbox, params_max, params_min, params_mean)
            with tab3:
                graph_bar(dataf.dataall)
                pass

st.divider()

with st.container(key='wrapperCalculator'):
    st.write('# Calculadora de Criptomonedas')
    st.write('###### ')
    ccol1, ccol2 = st.columns([1,1])
    with ccol1:
        calcu_inselectbox = st.selectbox('Selecciona la criptomoneda de entrada', dataf.names_index)
        calcu_innumber = st.number_input('')
    with ccol2:
        calcu_outselectbox = st.selectbox('Selecciona la criptomoneda de salida', dataf.names_index)
        calcu_outnumber = st.number_input('',value=dataf.cryto_calulator(calcu_inselectbox, calcu_outselectbox, calcu_innumber))



st.markdown(html_file, unsafe_allow_html=True)

