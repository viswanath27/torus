from flask import Flask, render_template, request
from charts import generate_candlestick_chart, generate_bar_chart, generate_line_chart, generate_figure_chart
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stock', methods=['POST'])
def stock():
    stock_name = request.form['stock_name']
    candlestick_chart = generate_candlestick_chart(stock_name)
    bar_chart = generate_bar_chart(stock_name)
    line_chart = generate_line_chart(stock_name)
    figure_chart = generate_figure_chart(stock_name)
    return render_template('stock.html', stock_name=stock_name, candlestick_chart=candlestick_chart,
                           bar_chart=bar_chart, line_chart=line_chart, figure_chart=figure_chart)
if __name__ == '__main__':
    app.run(debug=True)