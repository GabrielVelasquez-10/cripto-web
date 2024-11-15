import streamlit as st
import dataf
from streamlit_extras.metric_cards import style_metric_cards

def crypto_cards():
    col = st.columns(1)
    for name_files in dataf.csv_files:
        name_index = name_files[0:len(name_files)-4]
        col[0].metric(label=dataf.data[name_index]['Symbol'][0], value=f"${dataf.data[name_index]['Close'][-1:]}")
    style_metric_cards(background_color='#14141a', border_color='#00000000')
# endregion