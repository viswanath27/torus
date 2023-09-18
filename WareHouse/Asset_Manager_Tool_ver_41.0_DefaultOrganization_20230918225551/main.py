'''
This is the main file of the flask application. It initializes the Flask app, sets up the routes, and runs the application.
'''
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/fund_performance')
def fund_performance():
    # Collect data from Internet portals and generate the fund performance report
    # Implement the logic here
    return render_template('fund_performance.html')
if __name__ == '__main__':
    app.run(debug=True)