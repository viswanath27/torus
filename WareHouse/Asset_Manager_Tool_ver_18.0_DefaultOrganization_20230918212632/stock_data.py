'''
This file contains functions to retrieve stock data using the yfinance library.
'''
import yfinance as yf
def get_stock_data(stock_name, start_date, end_date):
    stock = yf.Ticker(stock_name)
    data = stock.history(start=start_date, end=end_date)
    return data