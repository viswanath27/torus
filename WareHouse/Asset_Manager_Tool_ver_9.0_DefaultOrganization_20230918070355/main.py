'''
This is the main file of the Flask application.
It contains the routes and logic for handling user requests.
'''
from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stock', methods=['POST'])
def stock():
    stock_name = request.form['stock_name']
    stock_data = yf.download(stock_name)
    if stock_data is None:
        error_message = f"Unable to retrieve stock data for {stock_name}. Please check the stock name and try again."
        return render_template('error.html', error_message=error_message)
    # Generate candlestick chart
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    fig.add_trace(go.Candlestick(x=stock_data.index,
                                 open=stock_data['Open'],
                                 high=stock_data['High'],
                                 low=stock_data['Low'],
                                 close=stock_data['Close']),
                  row=1, col=1)
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price')
    candlestick_html = fig.to_html(full_html=False)
    # Generate bar chart
    fig = go.Figure()
    fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], marker_color='green'))
    fig.update_layout(title='Bar Chart',
                      xaxis_title='Date',
                      yaxis_title='Volume')
    bar_html = fig.to_html(full_html=False)
    # Generate line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', marker_color='red'))
    fig.update_layout(title='Line Chart',
                      xaxis_title='Date',
                      yaxis_title='Price')
    line_html = fig.to_html(full_html=False)
    # Generate figure chart
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', marker_color='purple'),
                  row=1, col=1)
    fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], marker_color='orange', opacity=0.5),
                  row=2, col=1)
    fig.update_layout(title='Figure Chart',
                      xaxis_title='Date',
                      yaxis_title='Price/Volume')
    figure_html = fig.to_html(full_html=False)
    return render_template('stock.html', stock_name=stock_name, candlestick_html=candlestick_html, bar_html=bar_html, line_html=line_html, figure_html=figure_html)
if __name__ == '__main__':
    app.run(debug=True)