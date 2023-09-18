'''
This is the main file of the Flask application.
'''
from flask import Flask, render_template
import yfinance as yf
app = Flask(__name__)
@app.route('/')
def home():
    # Read stock data for APPLE organization using yfinance library
    stock_data = yf.download('AAPL')
    return render_template('home.html', stock_data=stock_data)
if __name__ == '__main__':
    app.run(debug=True)