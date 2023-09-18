# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def main():
	return render_template("main.html")

@app.route('/result', methods=['POST'])
def result():
    try:
        number = float(request.form['number'])
        squared = number ** 2
        return render_template('result.html', number=number, squared=squared)
    except ValueError:
        return "Invalid input. Please enter a number."

@app.route('/home')
def home():
      return render_template("home.html")

@app.route('/about')
def about():
      return render_template("about.html")
@app.route('/contact')
def contact():
      return render_template("contact.html")


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     user_input = request.form.get('user_input')
#     print(user_input)  # or process the input as needed
#     return redirect(url_for('home'))  # or redirect to another route

@app.route('/submit_form', methods=['POST'])
def submit_form():
    project_name = request.form.get('project_name')
    user_input = request.form.get('user_input')
    print("Project Name:", project_name)
    print("Description:", user_input)
    return redirect(url_for('home'))

'''
Give me the code for add fucntion in python
'''
@app.route('/add')
def add():
      return render_template("add.html")

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)


