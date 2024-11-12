# region import streamlit dependencies
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.metric_cards import style_metric_cards
# endregion

# region import global libreries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpl
import time as tm
import os
# endregion

st.set_page_config(layout="wide")


with st.spinner('Wait for it...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    csv_files = os.listdir('csv_files')
    tm.sleep(0.3)

# region Data function
def csv_data():
    data = {}
    data_index = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    for name_files in csv_files:
        name_index = name_files[0:len(name_files)-4]
        data[name_index] = pd.read_csv(f'csv_files/{name_files}')
        # data[name_index] = data[name_index][data_index]
    return data
data = csv_data()
# endregion


# region View funcition

def crypto_cards():
    col = st.columns(1)
    for name_files in csv_files:
        name_index = name_files[0:len(name_files)-4]
        col[0].metric(label=data[name_index]['Symbol'][0], value=f"${data[name_index]['Open'][-1:].round(4)}")

        
    style_metric_cards(background_color='#14141a')
# endregion



with st.container(key='cards'): # Cryto cards container
    crypto_cards()


with st.container(key='wrapperGraph'):
    col1, col2 = st.columns([1, 3])
    with col1:
        with st.container(key='graphParam'):
            st.write('## EExtitt')
    with col2:
        with st.container(key='graphShow'):
            tab1, tab2 = st.tabs(['tab1', 'tab2'])
            with tab1:
                st.header('grafico 1')
                # mpl.plot()
            with tab2:
                st.header('graficos 2')   
                st.line_chart(data['coin_Aave']['Volume'])


with st.container():
    st.write('## Sub-title')

with st.sidebar:
    st.write('## Side-Bar')


st.markdown(html_file, unsafe_allow_html=True)

