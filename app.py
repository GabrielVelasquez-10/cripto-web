# region import streamlit dependencies
import streamlit as st
# endregion

# region import global libreries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time as tm
# endregion

import dataf
from viewf import crypto_cards

st.set_page_config(layout="wide")


with st.spinner('Wait for it...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    tm.sleep(0.3)



with st.container(key='cards'): # Cryto cards container
    crypto_cards()


with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([2, 5])
    with col1:
        with st.container(key='graphParam'):
            st.write('## Parameters')
            params_selectbox = st.selectbox('Select a crypto', dataf.names_index)
            params_max = st.checkbox('Max Value')
            params_min = st.checkbox('Min Value')
            params_mean = st.checkbox('Mean Value')
    with col2:
        with st.container(key='graphShow'):
            tab1, tab2 = st.tabs(['Candle Graph', 'Line Graph'])
            with tab1:
                cfig = go.Figure()
                cfig.add_trace(go.Candlestick(x=dataf.data[params_selectbox]['Date'], open=dataf.data[params_selectbox]['Open'], high=dataf.data[params_selectbox]['High'], low=dataf.data[params_selectbox]['Low'], close=dataf.data[params_selectbox]['Close']))
                if params_max:
                    cfig.add_hline(dataf.data[params_selectbox]['Close'].max(), line_color='#da2929')
                if params_min:
                     cfig.add_hline(dataf.data[params_selectbox]['Close'].min(), line_color='#29da79')
                if params_mean:
                     cfig.add_hline(dataf.data[params_selectbox]['Close'].mean(), line_color='#d429da')
                st.plotly_chart(cfig)
                st.header('grafico 1')
            with tab2:
                st.line_chart(dataf.data['coin_Aave']['Close'], color='#ffffff')

st.markdown(html_file, unsafe_allow_html=True)

