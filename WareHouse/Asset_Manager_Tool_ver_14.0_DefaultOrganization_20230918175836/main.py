'''
This is the main file of the Flask application.
It contains the endpoints for drawing the candlestick chart, bar chart, and line chart.
'''
from flask import Flask, request, jsonify
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import base64
app = Flask(__name__)
@app.route('/candlestick', methods=['GET'])
def draw_candlestick_chart():
    stock_name = request.args.get('stock_name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    try:
        data = yf.download(stock_name, start=start_date, end=end_date)
    except Exception as e:
        return jsonify({'error': str(e)})
    fig, ax = plt.subplots()
    ax.plot(data['Close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Candlestick Chart')
    ax.grid(True)
    candlestick = BytesIO()
    plt.savefig(candlestick, format='png')
    plt.close(fig)
    candlestick.seek(0)
    plot_url = base64.b64encode(candlestick.getvalue()).decode()
    return jsonify({'plot_url': plot_url})
@app.route('/bar', methods=['GET'])
def draw_bar_chart():
    stock_name = request.args.get('stock_name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    try:
        data = yf.download(stock_name, start=start_date, end=end_date)
    except Exception as e:
        return jsonify({'error': str(e)})
    fig, ax = plt.subplots()
    ax.bar(data.index, data['Volume'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    ax.set_title('Bar Chart')
    ax.grid(True)
    bar = BytesIO()
    plt.savefig(bar, format='png')
    plt.close(fig)
    bar.seek(0)
    plot_url = base64.b64encode(bar.getvalue()).decode()
    return jsonify({'plot_url': plot_url})
@app.route('/line', methods=['GET'])
def draw_line_chart():
    stock_name = request.args.get('stock_name')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    try:
        data = yf.download(stock_name, start=start_date, end=end_date)
    except Exception as e:
        return jsonify({'error': str(e)})
    fig, ax = plt.subplots()
    ax.plot(data['Close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Line Chart')
    ax.grid(True)
    line = BytesIO()
    plt.savefig(line, format='png')
    plt.close(fig)
    line.seek(0)
    plot_url = base64.b64encode(line.getvalue()).decode()
    return jsonify({'plot_url': plot_url})
if __name__ == '__main__':
    app.run()