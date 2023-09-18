'''
This file contains functions for displaying stock data and patterns.
'''
import matplotlib.pyplot as plt
import tkinter as tk
def display_stock_data(data):
    # Add your code here to display the stock data in a user-friendly format
    print(data)
def display_stock_patterns(patterns):
    # Add your code here to display the identified patterns
    for pattern in patterns:
        print(pattern)
def plot_stock_data(data):
    # Add your code here to plot the stock data
    plt.plot(data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Apple Stock Data')
    plt.show()