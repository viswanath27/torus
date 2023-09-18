'''
This is the main file for the Flask application.
'''
from flask import Flask, render_template, request
from stock_data import get_stock_data
from charts import generate_candlestick_chart, generate_bar_chart, generate_line_chart
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/stock', methods=['POST'])
def stock():
    stock_name = request.form['stock_name']
    start_date = '2022-09-01'
    end_date = '2023-08-31'
    stock_data = get_stock_data(stock_name, start_date, end_date)
    candlestick_chart_url = generate_candlestick_chart(stock_data)
    bar_chart_url = generate_bar_chart(stock_data)
    line_chart_url = generate_line_chart(stock_data)
    return render_template('stock.html', 
                           stock_name=stock_name, 
                           candlestick_chart_url=candlestick_chart_url, 
                           bar_chart_url=bar_chart_url, 
                           line_chart_url=line_chart_url)
if __name__ == '__main__':
    app.run(debug=True)