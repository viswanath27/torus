# ChatDev Stock Data Application User Manual

## Introduction

The ChatDev Stock Data Application is a Flask-based web application that allows users to retrieve and visualize stock data for a given organization. The application uses the Yfinance library in Python to fetch stock data from Yahoo Finance and renders three types of charts (Candlestick chart, bar chart, line chart) on a webpage.

## Main Functions

The main functions of the ChatDev Stock Data Application include:

1. Retrieving stock data: Users can enter the name of a stock (e.g., Apple) and select a start date (September 2023) and an end date (August 2022) to fetch the corresponding stock data.

2. Rendering charts: The application generates three types of charts (Candlestick chart, bar chart, line chart) based on the retrieved stock data and displays them on the webpage.

## Installation

To use the ChatDev Stock Data Application, follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install Flask and other dependencies: Open a terminal or command prompt and navigate to the directory where the application files are located. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Start the application: Run the following command to start the Flask application:

   ```
   python main.py
   ```

   The application will start running on http://localhost:5000/

## Usage

Once the ChatDev Stock Data Application is running, follow these steps to use it:

1. Open a web browser and go to http://localhost:5000/

2. On the homepage, you will see a form with a field to enter the stock name. Enter the name of the stock you want to retrieve data for (e.g., Apple).

3. Click the "Submit" button.

4. The application will fetch the stock data from Yahoo Finance using the Yfinance library and generate the three charts (Candlestick chart, bar chart, line chart) based on the retrieved data.

5. The webpage will display the stock name and the three charts.

## Example

Here is an example of how to use the ChatDev Stock Data Application:

1. Open a web browser and go to http://localhost:5000/

2. Enter "Apple" in the stock name field.

3. Click the "Submit" button.

4. The application will fetch the stock data for Apple from September 2023 to August 2022 and generate the three charts.

5. The webpage will display the stock name as "Apple" and show the Candlestick chart, bar chart, and line chart.

## Conclusion

The ChatDev Stock Data Application is a Flask-based web application that allows users to retrieve and visualize stock data. By following the installation and usage instructions provided in this user manual, you can easily use the application to fetch stock data and view the corresponding charts.