'''
This is the main file of the Flask application.
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
    start_date = '2023-09-01'
    end_date = '2022-08-31'
    stock_data = get_stock_data(stock_name, start_date, end_date)
    candlestick_chart = generate_candlestick_chart(stock_data)
    bar_chart = generate_bar_chart(stock_data)
    line_chart = generate_line_chart(stock_data)
    return render_template('stock.html', stock_name=stock_name, 
                           candlestick_chart=candlestick_chart, 
                           bar_chart=bar_chart, line_chart=line_chart)
if __name__ == '__main__':
    app.run(debug=True)