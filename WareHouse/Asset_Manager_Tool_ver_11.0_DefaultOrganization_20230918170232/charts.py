import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def generate_candlestick_chart(stock_name):
    data = yf.download(stock_name, start='2022-09-01', end='2023-08-31')
    fig, ax = plt.subplots()
    ax.set_title(f'Candlestick Chart for {stock_name}')
    ax.plot(data['Close'], color='black', label='Close')
    ax.plot(data['Open'], color='green', label='Open')
    ax.plot(data['High'], color='red', label='High')
    ax.plot(data['Low'], color='blue', label='Low')
    ax.legend()
    chart_image = BytesIO()
    plt.savefig(chart_image, format='png')
    chart_image.seek(0)
    encoded_image = base64.b64encode(chart_image.getvalue()).decode('utf-8')
    plt.close()
    return encoded_image
def generate_bar_chart(stock_name):
    data = yf.download(stock_name, start='2022-09-01', end='2023-08-31')
    fig, ax = plt.subplots()
    ax.set_title(f'Bar Chart for {stock_name}')
    ax.bar(data.index, data['Volume'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    chart_image = BytesIO()
    plt.savefig(chart_image, format='png')
    chart_image.seek(0)
    encoded_image = base64.b64encode(chart_image.getvalue()).decode('utf-8')
    plt.close()
    return encoded_image
def generate_line_chart(stock_name):
    data = yf.download(stock_name, start='2022-09-01', end='2023-08-31')
    fig, ax = plt.subplots()
    ax.set_title(f'Line Chart for {stock_name}')
    ax.plot(data['Close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    chart_image = BytesIO()
    plt.savefig(chart_image, format='png')
    chart_image.seek(0)
    encoded_image = base64.b64encode(chart_image.getvalue()).decode('utf-8')
    plt.close()
    return encoded_image
def generate_figure_chart(stock_name):
    data = yf.download(stock_name, start='2022-09-01', end='2023-08-31')
    fig, ax = plt.subplots()
    ax.set_title(f'Figure Chart for {stock_name}')
    ax.plot(data['Close'])
    ax.fill_between(data.index, data['Close'], color='skyblue', alpha=0.3)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    chart_image = BytesIO()
    plt.savefig(chart_image, format='png')
    chart_image.seek(0)
    encoded_image = base64.b64encode(chart_image.getvalue()).decode('utf-8')
    plt.close()
    return encoded_image