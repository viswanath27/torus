'''
This module retrieves stock data using the yfinance library.
'''
import yfinance as yf
def get_stock_data(stock_name):
    stock = yf.Ticker(stock_name)
    data = stock.history(start='2022-09-01', end='2023-08-31')
    print(f'Data for {stock_name} retrieved successfully! {data}')
    return data