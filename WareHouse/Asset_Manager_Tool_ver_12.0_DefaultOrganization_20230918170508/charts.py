# '''
# This module contains functions to draw different types of charts using the matplotlib library.
# '''
import matplotlib.pyplot as plt
import mplfinance as mpf
import io
import base64
from flask import Flask, render_template_string
# def draw_candlestick_chart(stock_data):
#     '''
#     Draw a candlestick chart using the given stock data.
#     '''
#     print(stock_data)
#     mpf.plot(stock_data, type='candle')
# def draw_bar_chart(stock_data):
#     '''
#     Draw a bar chart using the given stock data.
#     '''
#     plt.bar(stock_data.index, stock_data['Close'])
#     plt.title('Bar Chart')
#     plt.show()
# def draw_line_chart(stock_data):
#     '''
#     Draw a line chart using the given stock data.
#     '''
#     plt.plot(stock_data.index, stock_data['Close'])
#     plt.title('Line Chart')
#     plt.show()
# def draw_figure_chart(stock_data):
#     '''
#     Draw a figure chart using the given stock data.
#     '''
#     plt.figure(figsize=(10, 6))
#     plt.plot(stock_data.index, stock_data['Close'])
#     plt.title('Figure Chart')
#     plt.show()

# @app.route('/candlestick')
def draw_candlestick_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    mpf.plot(stock_data, type='candle', savefig=buf)
    buf.seek(0)
    return render_chart(buf)

# @app.route('/bar')
def draw_bar_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.bar(stock_data.index, stock_data['Close'])
    plt.title('Bar Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)

# @app.route('/line')
def draw_line_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.plot(stock_data.index, stock_data['Close'])
    plt.title('Line Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)

# @app.route('/figure')
def draw_figure_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'])
    plt.title('Figure Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)
def render_chart(buf):
    """Renders the chart as an embedded image in an HTML page."""
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template_string(f'<img src="data:image/png;base64,{data}" />')