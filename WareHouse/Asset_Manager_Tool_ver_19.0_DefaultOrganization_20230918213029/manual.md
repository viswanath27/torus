# ChatDev Stock Analysis Application

The ChatDev Stock Analysis Application is a Flask application that allows users to retrieve and analyze stock data using the Yfinance library in Python. The application provides three types of charts - Candlestick chart, bar chart, and line chart - to visualize the stock data.

## Installation

To install the ChatDev Stock Analysis Application, follow the steps below:

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

To use the ChatDev Stock Analysis Application, follow the steps below:

1. Start the Flask application:

   ```
   python main.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter the name of the stock (e.g., Apple) in the input field and click the "Submit" button.

4. The application will retrieve the stock data for the given organization from September 2022 to August 2023 using the Yfinance library.

5. The application will generate and display the Candlestick chart, bar chart, and line chart for the stock data.

6. You can analyze the stock data using the provided charts and make informed decisions.

## Example

Here is an example of how to use the ChatDev Stock Analysis Application:

1. Start the Flask application:

   ```
   python main.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter the name of the stock (e.g., Apple) in the input field and click the "Submit" button.

4. The application will retrieve the stock data for Apple from September 2022 to August 2023.

5. The application will generate and display the Candlestick chart, bar chart, and line chart for the Apple stock data.

6. Analyze the charts to gain insights into the stock's performance and make informed investment decisions.

## Support

If you encounter any issues or have any questions, please reach out to our support team at support@chatdev.com. We are here to help you!

## License

The ChatDev Stock Analysis Application is licensed under the MIT License. See the [LICENSE](https://github.com/ChatDev/stock-analysis-app/blob/main/LICENSE) file for more information.