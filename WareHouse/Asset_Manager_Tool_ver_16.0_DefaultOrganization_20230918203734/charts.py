'''
This file contains functions to generate different types of charts using the matplotlib library.
'''
import os
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import url_for
def generate_candlestick_chart(stock_data):
    fig, ax = plt.subplots()
    ax.set_title('Candlestick Chart')
    ax.plot(stock_data['Close'], color='black')
    ax.xaxis_date()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Save the figure as a PNG image
    chart_path = os.path.join('static','images', 'candlestick_chart.png')
    plt.savefig(chart_path)
    # Return the image URL
    return url_for('static', filename='candlestick_chart.png')
def generate_bar_chart(stock_data):
    fig, ax = plt.subplots()
    ax.set_title('Bar Chart')
    ax.bar(stock_data.index, stock_data['Volume'])
    ax.xaxis_date()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Save the figure as a PNG image
    chart_path = os.path.join('static','images', 'bar_chart.png')
    plt.savefig(chart_path)
    # Return the image URL
    return url_for('static', filename='bar_chart.png')
def generate_line_chart(stock_data):
    fig, ax = plt.subplots()
    ax.set_title('Line Chart')
    ax.plot(stock_data['Close'], color='blue')
    ax.xaxis_date()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Save the figure as a PNG image
    chart_path = os.path.join('static','images', 'line_chart.png')
    plt.savefig(chart_path)
    # Return the image URL
    return url_for('static', filename='line_chart.png')