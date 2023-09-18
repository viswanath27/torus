'''
This is the main file for the Flask application.
'''
from flask import Flask, render_template
import yfinance as yf
app = Flask(__name__)
def fetch_stock_data():
    '''
    This function fetches the stock data using yfinance.
    '''
    return yf.download('AAPL', start='2022-09-01', end='2023-08-31')
stock_data = fetch_stock_data()
@app.route('/candlestick')
def candlestick():
    '''
    This route displays the candlestick chart.
    '''
    return render_template('candlestick.html', stock_data=stock_data)
@app.route('/bar')
def bar():
    '''
    This route displays the bar chart.
    '''
    return render_template('bar.html', stock_data=stock_data)
@app.route('/line')
def line():
    '''
    This route displays the line chart.
    '''
    return render_template('line.html', stock_data=stock_data)
@app.route('/figure')
def figure():
    '''
    This route displays the figure chart.
    '''
    return render_template('figure.html', stock_data=stock_data)
if __name__ == '__main__':
    app.run()