# ChatDev Stock Data Application User Manual

## Introduction

The ChatDev Stock Data Application is a Flask web application that allows users to view and analyze stock data for the Apple organization. The application utilizes the Yfinance library in Python to retrieve the stock data and presents it using various chart types, including Candlestick, Bar, Line, and Figure charts.

This user manual provides detailed instructions on how to install the necessary dependencies and how to use the application effectively.

## Installation

To install and run the ChatDev Stock Data Application, follow these steps:

1. Ensure that you have Python installed on your system. If not, download and install Python from the official Python website (https://www.python.org).

2. Clone or download the application code from the ChatDev repository.

3. Open a terminal or command prompt and navigate to the directory where you have downloaded the application code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the dependencies are installed, you are ready to run the application.

## Usage

To use the ChatDev Stock Data Application, follow these steps:

1. Ensure that you have completed the installation steps mentioned above.

2. In the terminal or command prompt, navigate to the directory where you have downloaded the application code.

3. Activate the virtual environment if you have created one (refer to step 5 of the installation instructions).

4. Run the following command to start the Flask application:

   ```
   python main.py
   ```

5. Open a web browser and enter the following URL:

   ```
   http://localhost:5000
   ```

6. The application's main page will be displayed, showing a form to enter the stock symbol.

7. Enter "AAPL" (the stock symbol for Apple) in the input field and click the "Get Data" button.

8. The application will retrieve the stock data using the Yfinance library and display a line chart showing the closing prices for the past year.

9. You can explore other chart types by modifying the code in the `index.html` and `script.js` files.

10. To stop the application, press `Ctrl + C` in the terminal or command prompt.

## Conclusion

Congratulations! You have successfully installed and used the ChatDev Stock Data Application. You can now explore and analyze Apple's stock data using various chart types. Feel free to customize the application further to suit your needs and explore additional functionalities.

If you encounter any issues or have any questions, please reach out to our support team for assistance. Happy analyzing!