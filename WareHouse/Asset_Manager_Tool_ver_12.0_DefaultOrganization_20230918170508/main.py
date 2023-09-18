'''
This is the main module of the Flask application.
'''
from flask import Flask, render_template, request
import stock_data
import charts
import matplotlib.pyplot as plt
import mplfinance as mpf
import io
import base64
from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def draw_candlestick_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    mpf.plot(stock_data, type='candle', savefig=buf)
    buf.seek(0)
    return render_chart(buf)

# @app.route('/bar')
def draw_bar_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.bar(stock_data.index, stock_data['Close'])
    plt.title('Bar Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)

# @app.route('/line')
def draw_line_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.plot(stock_data.index, stock_data['Close'])
    plt.title('Line Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)

# @app.route('/figure')
def draw_figure_chart(stock_data):
    # Fetch your stock data here.
    # stock_data = get_stock_data("AAPL")
    buf = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'])
    plt.title('Figure Chart')
    plt.savefig(buf, format='png')
    buf.seek(0)
    return render_chart(buf)
def render_chart(buf):
    """Renders the chart as an embedded image in an HTML page."""
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template_string(f'<img src="data:image/png;base64,{data}" />')
@app.route('/stock', methods=['POST'])
def stock():
    stock_name = request.form['stock_name']
    stock_data_result = stock_data.get_stock_data(stock_name)
    # charts.draw_candlestick_chart(stock_data_result)
    charts.draw_bar_chart(stock_data_result)
    # charts.draw_line_chart(stock_data_result)
    # charts.draw_figure_chart(stock_data_result)
    return 'Charts generated successfully!'
if __name__ == '__main__':
    app.run(debug=True, port=8090, threaded=False)