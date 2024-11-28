import streamlit as st
import dataf
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go

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

def graph_lines_params(max:bool=False, min:bool=False, mean:bool=False, data_index='', fig=None):
    if max:
        fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=[dataf.data[data_index]['Close'].max()]*len(dataf.data[data_index]), name='Valor Maximo'))
    if min:
        fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=[dataf.data[data_index]['Close'].min()]*len(dataf.data[data_index]), name='Valor Maximo'))
    if mean:
        fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=[dataf.data[data_index]['Close'].mean()]*len(dataf.data[data_index]), name='Valor de Media'))
 

def graph_candle(data_index, line_max, line_min, line_mean):
    fig = go.Figure()
    graph_lines_params(line_max, line_min, line_mean, data_index, fig)
    fig.add_trace(go.Candlestick(x=dataf.data[data_index]['Date'], open=dataf.data[data_index]['Open'], high=dataf.data[data_index]['High'], low=dataf.data[data_index]['Low'], close=dataf.data[data_index]['Close'], name='Valor del Mercado'))
    st.plotly_chart(fig)

def graph_line(data_index, line_max, line_min, line_mean):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataf.data[data_index]['Date'], y=dataf.data[data_index]['Close'], marker_color=color_primary, name='Valor del Mercado'))
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    graph_lines_params(line_max, line_min, line_mean, data_index, fig)
    st.plotly_chart(fig)

def graph_bar(data):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=data, x=dataf.names_index, marker_color=color_primary, name='Valor de los Mercados'))
    st.plotly_chart(fig)

def graph_pie(data_index):
    volatility = dataf.crypto_volatility(data_index)
    labels = ['Poco Volatil', 'Muy Volatil']
    values = [dataf.crypto_volatility('coin_Bitcoin', True)*1.34, volatility]
    colors = [color_secondary_backgound, color_primary]
    st.write('  Volatilidad del Mercado')
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, marker=dict(colors=colors))])
    fig.update(layout_showlegend=False)
    fig.update_layout(autosize=False,height=300, paper_bgcolor='rgba(0, 0, 0, 0)')
    st.plotly_chart(fig)

