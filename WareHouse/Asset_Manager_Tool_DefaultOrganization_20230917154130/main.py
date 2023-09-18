'''
This is the main file of the login flask application.
'''
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# User database
users = {
    'admin': 'password123'
}
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data here
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password are valid
        if username in users and users[username] == password:
            # Add your login logic here
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    # Add your dashboard logic here
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)