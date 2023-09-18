'''
Create a Flask application showing the Apple stock data with its patterns explained with the help of Candlestick chart, bar chart, line chart and figure chart. Use Yfinance library in python to read the stock data for APPLE organization.
'''
from flask import Flask, render_template, request, jsonify
import yfinance as yf
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stock_data', methods=['POST'])
def stock_data():
    symbol = request.form['symbol']
    stock = yf.Ticker(symbol)
    data = stock.history(period="1y")
    return jsonify(data.to_dict())
if __name__ == '__main__':
    app.run(debug=True)