# ChatDev Stock Analysis Application

## Introduction

The ChatDev Stock Analysis Application is a Flask-based web application that allows users to analyze stock data using the Yfinance library in Python. The application provides four different types of charts: Candlestick chart, bar chart, line chart, and figure chart. Each chart is displayed on a separate route, which can be accessed through the application's URL.

## Installation

To install and run the ChatDev Stock Analysis Application, follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/ChatDev/stock-analysis-app.git
   ```

2. Navigate to the project directory:

   ```
   cd stock-analysis-app
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
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

6. Run the Flask application:

   ```
   python main.py
   ```

7. Open your web browser and access the application at `http://localhost:5000`.

## Usage

Once the application is running, you can use it to analyze stock data by following these steps:

1. Enter the name of the stock you want to analyze in the input field provided on the home page.

2. Click on the "Submit" button.

3. The application will fetch the stock data using the Yfinance library and display the candlestick chart on the `/candlestick` route, the bar chart on the `/bar` route, the line chart on the `/line` route, and the figure chart on the `/figure` route.

4. To view a specific chart, simply navigate to the corresponding route in your web browser. For example, to view the candlestick chart, go to `http://localhost:5000/candlestick`.

## Example

Let's say you want to analyze the stock data for Apple. Here's how you can do it using the ChatDev Stock Analysis Application:

1. Enter "AAPL" in the input field on the home page.

2. Click on the "Submit" button.

3. Open a new tab in your web browser and go to `http://localhost:5000/candlestick` to view the candlestick chart.

4. Similarly, you can access the bar chart at `http://localhost:5000/bar`, the line chart at `http://localhost:5000/line`, and the figure chart at `http://localhost:5000/figure`.

## Conclusion

The ChatDev Stock Analysis Application provides an easy-to-use interface for analyzing stock data using the Yfinance library. With its four different types of charts, you can visualize the stock data in various ways and gain insights into the market trends. Install the application, enter the stock name, and start exploring the charts to make informed investment decisions.