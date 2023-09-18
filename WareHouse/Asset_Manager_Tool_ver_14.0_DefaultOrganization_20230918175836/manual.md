# ChatDev Flask Stock Chart Application User Manual

## Introduction

The ChatDev Flask Stock Chart Application is a web application built with Flask that allows users to retrieve and visualize stock data using the Yfinance library in Python. The application provides endpoints for drawing candlestick charts, bar charts, and line charts for a given stock.

This user manual provides detailed instructions on how to install the necessary dependencies and how to use the application to retrieve and visualize stock data.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Candlestick Chart](#candlestick-chart)
   - [Bar Chart](#bar-chart)
   - [Line Chart](#line-chart)
3. [API Endpoints](#api-endpoints)
   - [/candlestick](#candlestick-endpoint)
   - [/bar](#bar-endpoint)
   - [/line](#line-endpoint)

## Installation <a name="installation"></a>

To install the ChatDev Flask Stock Chart Application, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:

   ```
   git clone https://github.com/ChatDev/Flask-Stock-Chart-Application.git
   ```

4. Navigate to the project directory:

   ```
   cd Flask-Stock-Chart-Application
   ```

5. Create a virtual environment to isolate the application's dependencies:

   ```
   python -m venv venv
   ```

6. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source venv/bin/activate
     ```

7. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

8. The installation is now complete.

## Usage <a name="usage"></a>

To use the ChatDev Flask Stock Chart Application, follow these steps:

1. Make sure you have completed the installation steps mentioned above.

2. Start the Flask application by running the following command:

   ```
   python main.py
   ```

   The application will start running on `http://localhost:5000`.

3. Open a web browser and navigate to `http://localhost:5000`.

### Candlestick Chart <a name="candlestick-chart"></a>

To draw a candlestick chart for a stock, follow these steps:

1. Enter the stock name in the input field.

2. Enter the start date and end date in the format `YYYY-MM-DD`.

3. Click the "Draw Candlestick Chart" button.

4. The candlestick chart will be displayed on the page.

### Bar Chart <a name="bar-chart"></a>

To draw a bar chart for a stock, follow these steps:

1. Enter the stock name in the input field.

2. Enter the start date and end date in the format `YYYY-MM-DD`.

3. Click the "Draw Bar Chart" button.

4. The bar chart will be displayed on the page.

### Line Chart <a name="line-chart"></a>

To draw a line chart for a stock, follow these steps:

1. Enter the stock name in the input field.

2. Enter the start date and end date in the format `YYYY-MM-DD`.

3. Click the "Draw Line Chart" button.

4. The line chart will be displayed on the page.

## API Endpoints <a name="api-endpoints"></a>

The ChatDev Flask Stock Chart Application provides the following API endpoints:

### /candlestick <a name="candlestick-endpoint"></a>

This endpoint allows you to draw a candlestick chart for a stock.

- Method: GET
- Parameters:
  - stock_name: The name of the stock (e.g., "Apple")
  - start_date: The start date in the format `YYYY-MM-DD`
  - end_date: The end date in the format `YYYY-MM-DD`
- Response: JSON object with the plot URL

Example usage:

```
GET /candlestick?stock_name=Apple&start_date=2022-09-01&end_date=2023-08-31
```

### /bar <a name="bar-endpoint"></a>

This endpoint allows you to draw a bar chart for a stock.

- Method: GET
- Parameters:
  - stock_name: The name of the stock (e.g., "Apple")
  - start_date: The start date in the format `YYYY-MM-DD`
  - end_date: The end date in the format `YYYY-MM-DD`
- Response: JSON object with the plot URL

Example usage:

```
GET /bar?stock_name=Apple&start_date=2022-09-01&end_date=2023-08-31
```

### /line <a name="line-endpoint"></a>

This endpoint allows you to draw a line chart for a stock.

- Method: GET
- Parameters:
  - stock_name: The name of the stock (e.g., "Apple")
  - start_date: The start date in the format `YYYY-MM-DD`
  - end_date: The end date in the format `YYYY-MM-DD`
- Response: JSON object with the plot URL

Example usage:

```
GET /line?stock_name=Apple&start_date=2022-09-01&end_date=2023-08-31
```

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev Flask Stock Chart Application. You can now retrieve and visualize stock data using the provided endpoints. Enjoy exploring the world of stock charts!