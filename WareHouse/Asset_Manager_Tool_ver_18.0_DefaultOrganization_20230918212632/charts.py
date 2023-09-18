'''
This file contains functions to generate different types of charts using the plotly library.
'''
import plotly.graph_objects as go
def generate_candlestick_chart(stock_data):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])
    return fig.to_html(full_html=False)
def generate_bar_chart(stock_data):
    fig = go.Figure(data=[go.Bar(x=stock_data.index, y=stock_data['Volume'])])
    return fig.to_html(full_html=False)
def generate_line_chart(stock_data):
    fig = go.Figure(data=[go.Scatter(x=stock_data.index, y=stock_data['Close'])])
    return fig.to_html(full_html=False)