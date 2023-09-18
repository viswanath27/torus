# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, redirect, url_for, stream_with_context, Response, session,send_from_directory
# from chatdev_app import run_chat_chain_project
# from celery import Celery
import jsonify 
import subprocess 
import uuid
from threading import Thread
from collections import deque
import time
import queue
import threading
import os
import zipfile
# Use a deque as a buffer; this holds the last n lines
BUFFER_SIZE = 1000  # or whatever you require
buffer = deque(maxlen=BUFFER_SIZE)
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
app.secret_key = uuid.uuid4().hex
process = None
logs_queue = queue.Queue()

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
#       def generate():
#             project_name = request.form.get('project_name')
#             user_input = request.form.get('user_input')
#             # Start a new process for the long-running task
#             process = subprocess.Popen(["python", "chatdev_app.py", "--task", user_input, "--name", project_name])
#             for line in iter(process.stdout.readline, b''):
#                   decoded_line = line.decode('utf-8')
#                   yield f"data: {decoded_line}<br>\n\n"
#                   # time.sleep(0.1)  # to throttle for demonstration
#             # return jsonify({"message": "Request submitted"}), 202
#             # return render_template("home.html")
#       return Response(generate(), mimetype='text/event-stream')
        
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Store form data in global or another mechanism (like database, cache, etc.) 
    # for the log stream to access.
#     global project_name, user_input
    session['project_name'] = request.form.get('project_name')
    session['user_input'] = request.form.get('user_input')
    project_name = request.form.get('project_name')
    user_input = request.form.get('user_input')
    global process, logs_queue
    if not process or process.poll() is not None:
        process = subprocess.Popen(["python", "chatdev_app.py", "--task", user_input, "--name", project_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
        thread = threading.Thread(target=read_output, args=(process,))
        thread.start()
    return redirect(url_for('main'))
    #return jsonify({"message": "Request submitted"}), 202

@app.route('/download_zip', methods=['GET', 'POST'])
def download_zip():
#     folder_path = os.path.join(os.path.dirname(__file__), 'WareHouse',session['project_name']+"_DefaultOrganization"+"_")
    folder_path = "/Users/bossacct/work/torus_application/torus/WareHouse/Asset_Manager_Tool_ver_55.0_DefaultOrganization_20230918225927"

    # Ensure the folder exists
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return "Folder not found", 404

    # Create a zip filename based on folder name
    zip_filename = os.path.basename(folder_path) + '.zip'
    zip_path = os.path.join(os.path.dirname(folder_path), zip_filename)

    # Zip the folder
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                absolute_path = os.path.join(foldername, filename)
                relative_path = absolute_path[len(folder_path) + 1:]  # +1 to exclude leading slash
                zipf.write(absolute_path, relative_path)

    # Serve the zipped file to the user
    return send_from_directory(os.path.dirname(zip_path), zip_filename, as_attachment=True)

@app.route('/kill')
def kill_process():
    global process
    print(f'Process: {process}')
    if process and process.poll() is None:
        try:
            process.terminate()
            time.sleep(2)
            if process.poll() is None:
                process.kill()
        except Exception as e:
            print("Error terminating process:", e)
    return redirect(url_for('view_logs'))


# def subprocess_thread():
#     # Sample subprocess that prints numbers with a delay.
#     process = subprocess.Popen(["python", "chatdev_app.py", "--task", "Create a Flask application which can take the name of the stock (Ex: Apple) use Yfinance library in python to read the stock data for the given organization from Sept 2023 to Aug 2022. Draw following charts Candlestick chart, bar chart, line chart and figure chart", "--name", "Asset_Manager_Tool_ver_10.0"],
#                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     for line in iter(process.stdout.readline, b''):
#         decoded_line = line.decode('utf-8').strip()
#         buffer.append(decoded_line)
#         time.sleep(0.1)
#     # Start the subprocess in a separate thread
#     thread = Thread(target=subprocess_thread)
#     thread.start()
#     print("Thread started ")



# @app.route('/stream_logs')
# def stream_logs():
#     def generate():
#         # Yield the already generated logs first
#         for line in list(buffer):
#             yield f"data: {line}\n\n"
#             time.sleep(0.1)  # Delay for demo

#         # Then, continue yielding new logs as they come
#         while True:
#             if buffer and buffer[-1] != line:  # check if there's a new line in buffer
#                 line = buffer[-1]
#                 yield f"data: {line}\n\n"
#             time.sleep(1)

#     return Response(generate(), mimetype='text/event-stream')

def read_output(proc):
    for line in iter(proc.stdout.readline, ''):
        logs_queue.put(line)
        time.sleep(0.05)

@app.route('/logs')
def view_logs():
    return render_template('log.html')

@app.route('/logstream', methods=['GET'])
def log_stream():
    def generate():
        while True:
            log = logs_queue.get()
            yield f"data: {log}\n\n"

    return Response(generate(), content_type='text/event-stream')


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True,use_reloader=False,threaded=True,port=8080)


