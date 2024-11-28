# region import streamlit dependencies
import streamlit as st
# endregion

# region import global libreries
import pandas as pd
import plotly.graph_objects as go
import time as tm
# endregion

import dataf
from viewf import crypto_cards, graph_candle, graph_line, graph_bar, graph_pie
from datetime import datetime

st.set_page_config(layout="wide")
# st.image('Post_de_Instagram_podcast_negocios_formal-removebg-preview.png')

# spinner
with st.spinner('Cargando...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    st.markdown(html_file, unsafe_allow_html=True)
    tm.sleep(3)


with st.container(key='cards'): # Cryto cards container
    crypto_cards()

with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(key='graphParam'):
            st.write('## Parametros')
            params_selectbox = st.selectbox('Selecciona una criptomoneda', dataf.names_index)            
            
            st.write('#### Indicadores')
            params_max = st.checkbox('Max Value')
            params_mean = st.checkbox('Mean Value')
            params_min = st.checkbox('Min Value')
 
            graph_pie(params_selectbox)
            st.markdown(html_file, unsafe_allow_html=True)
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
        with st.container(key='graphInfo'):
            st.write('#### Titulo')
            st.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
            pass

with st.container(key='wrapperCalculator'):
    st.divider()
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