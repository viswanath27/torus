'''
This is the main file of the Flask application.
It handles the routing and rendering of the web pages.
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
    start_date = '2022-09-01'
    end_date = '2023-08-31'
    # Fetch stock data using yfinance library
    stock_data = yf.download(stock_name, start=start_date, end=end_date)
    # Process the stock data and generate charts
    candlestick_data = [
        go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close']
        )
    ]
    bar_data = [
        go.Bar(
            x=stock_data.index,
            y=stock_data['Volume']
        )
    ]
    line_data = [
        go.Scatter(
            x=stock_data.index,
            y=stock_data['Close']
        )
    ]
    print(candlestick_data)
    # Return the rendered stock page with charts
    return render_template('stock.html', stock_name=stock_name, candlestick_data=candlestick_data, bar_data=bar_data, line_data=line_data)
if __name__ == '__main__':
    app.run(debug=True)