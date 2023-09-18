'''
This is the main file of the flask application. It initializes the Flask app, sets up the routes, and runs the application.
'''
from flask import Flask, render_template
import data_collector
import fund_performance_report
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/fund_performance')
def fund_performance():
    data = data_collector.collect_data()
    report = fund_performance_report.generate_report(data)
    return render_template('fund_performance.html', report=report)
if __name__ == '__main__':
    app.run()