'''
This is the main file of the Flask application.
'''
from flask import Flask, render_template
import yfinance as yf
import datetime
app = Flask(__name__)
@app.route('/')
def home():
    # Specify the date range for the stock data
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    # Read stock data for APPLE organization using yfinance library
    apple_data = yf.download('AAPL', start=start_date, end=end_date)
    # Pass the stock data to the template for rendering
    return render_template('home.html', data=apple_data)
if __name__ == '__main__':
    app.run(debug=True)