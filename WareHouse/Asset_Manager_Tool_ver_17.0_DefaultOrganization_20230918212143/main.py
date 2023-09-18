'''
This is the main file of the Flask application.
It handles the routing and rendering of the webpages.
'''
from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objects as go
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stock', methods=['POST'])
def stock():
    stock_name = request.form['stock_name']
    start_date = '2023-09-01'
    end_date = '2022-08-31'
    stock_data = yf.download(stock_name, start=start_date, end=end_date)
    candlestick_chart = create_candlestick_chart(stock_data)
    bar_chart = create_bar_chart(stock_data)
    line_chart = create_line_chart(stock_data)
    return render_template('stock.html', 
                           stock_name=stock_name, 
                           candlestick_chart=candlestick_chart, 
                           bar_chart=bar_chart, 
                           line_chart=line_chart)
def create_candlestick_chart(stock_data):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])
    return fig.to_html(full_html=False)
def create_bar_chart(stock_data):
    fig = go.Figure(data=[go.Bar(x=stock_data.index, y=stock_data['Volume'])])
    return fig.to_html(full_html=False)
def create_line_chart(stock_data):
    fig = go.Figure(data=[go.Scatter(x=stock_data.index, y=stock_data['Close'])])
    return fig.to_html(full_html=False)
if __name__ == '__main__':
    app.run(debug=True)