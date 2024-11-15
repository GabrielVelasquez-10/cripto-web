# region import streamlit dependencies
import streamlit as st
# endregion

# region import global libreries
import pandas as pd
import plotly.graph_objects as go
import time as tm
# endregion

import dataf
import viewf

st.set_page_config(layout="wide")


with st.spinner('Wait for it...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    tm.sleep(0.3)



with st.container(key='cards'): # Cryto cards container
    viewf.crypto_cards()


with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(key='graphParam'):
            st.write('## Parameters')
            st.selectbox('select a option', dataf.names_index)
    with col2:
        with st.container(key='graphShow'):
            tab1, tab2 = st.tabs(['Candle Graph', 'Line Graph'])
            with tab1:
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=dataf.data['coin_Aave']['Date'], open=dataf.data['coin_Aave']['Open'], high=dataf.data['coin_Aave']['High'], low=dataf.data['coin_Aave']['Low'], close=dataf.data['coin_Aave']['Close']))
                st.plotly_chart(fig)
                st.header('grafico 1')
            with tab2:
                st.line_chart(dataf.data['coin_Aave']['Volume'], color='#ffffff')


with st.container():
    st.write('## Sub-title')

with st.sidebar:
    st.write('## Side-Bar')

st.markdown(html_file, unsafe_allow_html=True)

