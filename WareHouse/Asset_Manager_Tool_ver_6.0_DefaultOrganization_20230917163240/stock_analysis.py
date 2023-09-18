'''
This file contains functions for retrieving and analyzing stock data.
'''
import yfinance as yf
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1y")
    return data
def analyze_stock_data(data):
    patterns = []
    # Example pattern identification
    if data['Close'].iloc[-1] > data['Close'].iloc[-2]:
        patterns.append("Upward trend")
    else:
        patterns.append("Downward trend")
    return patterns