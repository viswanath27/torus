# Flask Stock Data Application

The Flask Stock Data Application is a web application that allows users to retrieve and visualize stock data for a given organization. It uses the Yfinance library in Python to fetch the stock data and generates four types of charts: Candlestick chart, bar chart, line chart, and figure chart.

## Installation

To use the Flask Stock Data Application, you need to have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, follow these steps to set up the application:

1. Clone the repository or download the source code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (optional but recommended) by running the following command:

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To start the Flask Stock Data Application, follow these steps:

1. Make sure you are in the project directory and the virtual environment is activated.

2. Run the following command to start the Flask development server:

   ```shell
   python main.py
   ```

3. Open a web browser and go to `http://localhost:5000` to access the application.

4. On the homepage, you will see a form where you can enter the name of the stock you want to retrieve data for. Enter the stock name and click the "Submit" button.

5. The application will fetch the stock data using the Yfinance library and generate four charts: Candlestick chart, bar chart, line chart, and figure chart.

6. The stock data and charts will be displayed on the stock details page. You can navigate back to the homepage to fetch data for another stock.

## File Structure

The Flask Stock Data Application consists of the following files:

- `main.py`: The main file of the Flask application that contains the routes and logic for handling user requests.

- `templates/index.html`: The HTML template for the homepage of the application.

- `templates/stock.html`: The HTML template for the stock details page of the application.

- `templates/error.html`: The HTML template for displaying error messages.

- `requirements.txt`: The file that lists the required dependencies for the application.

## Dependencies

The Flask Stock Data Application requires the following dependencies:

- Flask: A micro web framework for Python.

- yfinance: A Python library to fetch stock market data from Yahoo Finance.

- plotly: A graphing library for creating interactive and customizable charts.

These dependencies are listed in the `requirements.txt` file and can be installed using the `pip` package manager.

## Conclusion

The Flask Stock Data Application is a simple and user-friendly web application that allows users to retrieve and visualize stock data. It provides four types of charts to help users analyze the stock performance. By following the installation and usage instructions provided in this manual, you can easily set up and use the application to fetch stock data for any organization of your choice.