import streamlit as st
import dataf
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

# Page color config
color_primary = '#7f36db'
color_background = '#181818'
color_secondary_backgound = '#281f32'
color_font = '#fafafa'
font = ''

def crypto_cards():
    col = st.columns(1)
    for name_files in dataf.csv_files:
        name_index = name_files[0:len(name_files)-4]
        col[0].metric(label=dataf.data[name_index]['Symbol'][0], value=f"${dataf.data[name_index]['Close'][-1:]}")
    style_metric_cards(background_color=color_secondary_backgound, border_color='#00000000', border_left_color=color_primary)

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
    fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=dataf.data[data_index]['Close'], marker_color=color_primary))
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
    fig.add_trace(go.Bar(y=data, x=dataf.names_index, marker_color=color_primary))
    st.plotly_chart(fig)

def graph_pie():
    labels = ['Poco Confiable', 'Muy Confiable']
    values = [4500, 2500]
    colors = [color_primary, color_secondary_backgound]

    # Use `hole` to create a donut-like pie chart
    st.write('  Confiabilidad de Inversion')
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,marker=dict(colors=colors))])
    fig.update(layout_showlegend=False)
    fig.update_layout(autosize=False,height=300, paper_bgcolor='rgba(0, 0, 0, 0)')
    st.plotly_chart(fig)


