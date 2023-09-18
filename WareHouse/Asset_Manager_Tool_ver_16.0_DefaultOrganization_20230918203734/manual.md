# ChatDev Stock Data Flask Application User Manual

## Introduction

Welcome to the user manual for the ChatDev Stock Data Flask Application! This application allows you to retrieve and visualize stock data for a given organization using the Yfinance library in Python. You can view the stock data in three different types of charts: Candlestick chart, Bar chart, and Line chart.

## Table of Contents

1. Installation
2. Usage
3. Dependencies
4. File Structure
5. Troubleshooting

## 1. Installation

To install the ChatDev Stock Data Flask Application, follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/your-username/chatdev-stock-data-flask-app.git
   ```

2. Change into the project directory:

   ```
   cd chatdev-stock-data-flask-app
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Start the Flask application:

   ```
   python main.py
   ```

7. Open your web browser and navigate to `http://localhost:5000` to access the application.

## 2. Usage

Once you have the ChatDev Stock Data Flask Application up and running, you can follow these steps to retrieve and visualize stock data:

1. Enter the name of the stock in the "Stock Name" input field on the homepage.

2. Click the "Submit" button.

3. The application will retrieve the stock data for the given organization from September 2022 to August 2023 using the Yfinance library.

4. The application will generate three charts: Candlestick chart, Bar chart, and Line chart.

5. The charts will be displayed on the stock data page along with the stock name.

6. You can navigate back to the homepage by clicking the "Home" link.

## 3. Dependencies

The ChatDev Stock Data Flask Application relies on the following dependencies:

- Flask==2.0.1
- yfinance==0.1.63
- matplotlib==3.4.3
- pandas==1.3.3

These dependencies are automatically installed when you run `pip install -r requirements.txt` as mentioned in the installation steps.

## 4. File Structure

The file structure of the ChatDev Stock Data Flask Application is as follows:

- `main.py`: The main file for the Flask application.
- `stock_data.py`: Contains functions to retrieve stock data using the Yfinance library.
- `charts.py`: Contains functions to generate different types of charts using the Matplotlib library.
- `templates/index.html`: The homepage HTML template.
- `templates/stock.html`: The stock data page HTML template.
- `static/candlestick_chart.png`: The generated candlestick chart image.
- `static/bar_chart.png`: The generated bar chart image.
- `static/line_chart.png`: The generated line chart image.
- `requirements.txt`: The list of dependencies required by the application.

## 5. Troubleshooting

If you encounter any issues while using the ChatDev Stock Data Flask Application, consider the following troubleshooting steps:

1. Make sure you have installed all the required dependencies as mentioned in the installation steps.

2. Check that the stock name you entered is valid and corresponds to a publicly traded organization.

3. Verify that you have an active internet connection to retrieve the stock data.

4. If the charts are not displaying properly, ensure that the Matplotlib library is installed correctly.

If the issue persists, please reach out to our support team for further assistance.

---

Congratulations! You have successfully installed and learned how to use the ChatDev Stock Data Flask Application. Enjoy exploring and visualizing stock data with ease!