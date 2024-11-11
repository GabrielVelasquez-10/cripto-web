# region import streamlit dependencies
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.metric_cards import style_metric_cards
# endregion

# region import global libreries
import pandas as pd
import matplotlib.pyplot as plt
import time as tm
import os
# endregion

# region View funcition
def crypto_cards():
    col = st.columns(1)
    for i in range(8):
        col[0].metric(label='Hola', value=20.2)
    style_metric_cards(background_color='#14141a')
# endregion

# region Data function
def data():
    data = {}
    for name_files in csv_files:
        name_index = name_files[0:len(name_files)-4]
        st.write(name_index)
        data[name_index] = pd.read_csv(f'csv_files/{name_files}')
        st.write(name_index)
    return data
# endregion

with st.spinner('Wait for it...'): # loading page
    with open('custom.html') as file: # read html custom styles
        html_file = file.read()
    csv_files = os.listdir('csv_files')
    tm.sleep(0.3)


with st.container(key='cards'): # Cryto cards container
    crypto_cards()

with st.container():
    st.title('Hola mundo')

with st.container():
    st.write('## Sub-title')


st.markdown(html_file, unsafe_allow_html=True)

