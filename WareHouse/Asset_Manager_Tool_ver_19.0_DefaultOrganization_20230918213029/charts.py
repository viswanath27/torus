'''
Module for generating different types of charts using matplotlib library.
'''
import matplotlib.pyplot as plt
def generate_candlestick_chart(stock_data):
    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], color='black')
    ax.set_title('Candlestick Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.grid(True)
    return fig
def generate_bar_chart(stock_data):
    fig, ax = plt.subplots()
    ax.bar(stock_data.index, stock_data['Volume'])
    ax.set_title('Bar Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    ax.grid(True)
    return fig
def generate_line_chart(stock_data):
    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], color='blue')
    ax.set_title('Line Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.grid(True)
    return fig