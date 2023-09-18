# ChatDev Stock Charts Application User Manual

## Introduction

Welcome to the ChatDev Stock Charts Application! This Flask application allows you to retrieve and visualize stock data using the Yfinance library in Python. With this application, you can generate candlestick charts, bar charts, line charts, and figure charts for a given stock.

## Installation

To use the ChatDev Stock Charts Application, you need to set up the environment and install the required dependencies. Here are the steps to install the application:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/chatdev/stock-charts-app.git
   ```

2. Navigate to the project directory:

   ```
   cd stock-charts-app
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

## Usage

Once you have installed the application, you can start using it to generate stock charts. Here's how to use the ChatDev Stock Charts Application:

1. Run the Flask application:

   ```
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. You will see a form where you can enter the name of the stock you want to retrieve data for.

4. Enter the stock name and click the "Generate Charts" button.

5. The application will retrieve the stock data using the Yfinance library and generate the following charts:

   - Candlestick chart
   - Bar chart
   - Line chart
   - Figure chart

6. The charts will be displayed on the web page.

7. You can repeat the process to generate charts for different stocks.

## Example

Let's say you want to generate stock charts for Apple. Here's how you can do it:

1. Run the Flask application:

   ```
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter "Apple" in the stock name field.

4. Click the "Generate Charts" button.

5. The application will retrieve the stock data for Apple using the Yfinance library and generate the charts.

6. The charts will be displayed on the web page.

7. You can explore the different charts and analyze the stock data.

## Conclusion

Congratulations! You have successfully installed and used the ChatDev Stock Charts Application. Now you can retrieve and visualize stock data using the Yfinance library in Python. Enjoy exploring the stock charts and analyzing the data!

If you have any questions or need further assistance, please don't hesitate to contact our support team.