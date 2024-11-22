import streamlit as st
import dataf
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

color_main = '#ff4b4b'

def crypto_cards():
    col = st.columns(1)
    for name_files in dataf.csv_files:
        name_index = name_files[0:len(name_files)-4]
        col[0].metric(label=dataf.data[name_index]['Symbol'][0], value=f"${dataf.data[name_index]['Close'][-1:]}")
    style_metric_cards(background_color='#262730', border_color='#00000000', border_left_color='#ff4b4b')

def graph_candle(data_index, line_max, line_min, line_mean):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataf.data[data_index]['Date'], open=dataf.data[data_index]['Open'], high=dataf.data[data_index]['High'], low=dataf.data[data_index]['Low'], close=dataf.data[data_index]['Close']))
    if line_max:
        fig.add_hline(dataf.data[data_index]['Close'].max(), line_color='#da2929')
    if line_min:
            fig.add_hline(dataf.data[data_index]['Close'].min(), line_color='#29da79')
    if line_mean:
            fig.add_hline(dataf.data[data_index]['Close'].mean(), line_color='#d429da')
    st.plotly_chart(fig)

def graph_line(data_index, line_max, line_min, line_mean):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=dataf.data[data_index]['Close'], marker_color=color_main))
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    if line_max:
        fig.add_hline(dataf.data[data_index]['Close'].max(), line_color='#da2929')
    if line_min:
            fig.add_hline(dataf.data[data_index]['Close'].min(), line_color='#29da79')
    if line_mean:
            fig.add_hline(dataf.data[data_index]['Close'].mean(), line_color='#d429da')
    st.plotly_chart(fig)

def graph_bar(data):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=data, x=dataf.names_index, marker_color=color_main))
    # st.write(data)
    st.plotly_chart(fig)

def graph_pie():
    labels = ['Poco Confiable','Medianamente Confiable','Muy Confiable']
    values = [4500, 2500, 1053]
    colors = ['#ff4b4b','#ffde4b','#4bff5a']

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,marker=dict(colors=colors))])
    fig.update(layout_showlegend=False)
    fig.update_layout(autosize=False,height=300)
    st.plotly_chart(fig)

