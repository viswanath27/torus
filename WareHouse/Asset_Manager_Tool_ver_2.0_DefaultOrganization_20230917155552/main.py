'''
This is the main file of the flask application.
'''
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/fund_performance')
def fund_performance():
    # Collect data from Internet portals and generate the fund performance report
    # Replace this code with the actual implementation
    report_data = {
        'fund_name': 'BajajAlliance Mutual Fund',
        'performance': {
            'yearly': [10, 15, 12, 8, 9],
            'monthly': [1, 2, 3, 4, 5]
        }
    }
    return render_template('fund_performance.html', data=report_data)
if __name__ == '__main__':
    app.run(debug=True)