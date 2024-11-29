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

logo = 'logo-web.svg'
st.set_page_config(page_title='Crypto Web', page_icon=logo, layout="wide")

# spinner
with st.spinner('Cargando...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    st.markdown(html_file, unsafe_allow_html=True)
    tm.sleep(3)


st.image(logo, width=60)

with st.container(key='cards'): # Cryto cards container
    crypto_cards()

with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(key='graphParam'):
            st.write('## Parametros')
            params_selectbox = st.selectbox('Selecciona una criptomoneda', dataf.names_index)            
            
            st.write('#### Indicadores')
            params_max = st.checkbox('Valor Maximo')
            params_mean = st.checkbox('Valor de Media')
            params_min = st.checkbox('Valor Minimo')
 
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
                with st.container(key='graphBar'):
                    graph_bar(dataf.dataall)
                pass
        with st.container(key='graphInfo'):
            st.write('##### Nota:')
            st.write('- El porcentaje de volatilidad indica que tipo de inversion ejecutar en el mercado seleccionado')
            pass

with st.container(key='wrapperCalculator'):
    st.divider()
    st.write('# Calculadora de Criptomonedas')
    st.write('###### ')
    ccol1, ccol2 = st.columns([1,1])
    with ccol1:
        calcu_inselectbox = st.selectbox('Selecciona la criptomoneda de entrada', dataf.names_index)
        calcu_innumber = st.number_input('', value=1)
    with ccol2:
        calcu_outselectbox = st.selectbox('Selecciona la criptomoneda de salida', dataf.names_index)
        calcu_outnumber = st.number_input('',value=dataf.cryto_calulator(calcu_inselectbox, calcu_outselectbox, calcu_innumber))
st.markdown(html_file, unsafe_allow_html=True)