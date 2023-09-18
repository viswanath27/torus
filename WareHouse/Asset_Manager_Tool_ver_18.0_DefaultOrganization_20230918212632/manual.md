# ChatDev Stock Data Application User Manual

## Introduction

The ChatDev Stock Data Application is a Flask-based web application that allows users to retrieve and visualize stock data for a given organization. The application uses the Yfinance library in Python to fetch stock data and generates three types of charts: Candlestick chart, bar chart, and line chart. This user manual provides detailed instructions on how to install the application and how to use its main features.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Starting the Application](#starting-the-application)
   - [Retrieving Stock Data](#retrieving-stock-data)
   - [Viewing Charts](#viewing-charts)
3. [Dependencies](#dependencies)
4. [Support](#support)

## Installation <a name="installation"></a>

To install the ChatDev Stock Data Application, follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/ChatDev/stock-data-application.git
   ```

2. Navigate to the project directory:

   ```
   cd stock-data-application
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

6. The installation is now complete.

## Usage <a name="usage"></a>

### Starting the Application <a name="starting-the-application"></a>

To start the ChatDev Stock Data Application, follow these steps:

1. Make sure you are in the project directory and the virtual environment is activated (if used).

2. Run the following command:

   ```
   python main.py
   ```

3. The Flask application will start running on `http://localhost:5000`.

### Retrieving Stock Data <a name="retrieving-stock-data"></a>

To retrieve stock data for a specific organization, follow these steps:

1. Open a web browser and go to `http://localhost:5000`.

2. You will see a form asking for the stock name. Enter the name of the organization (e.g., "Apple") and click the "Submit" button.

3. The application will fetch the stock data using the Yfinance library and generate the charts.

### Viewing Charts <a name="viewing-charts"></a>

After retrieving the stock data, you can view the three types of charts: Candlestick chart, bar chart, and line chart. Follow these steps:

1. Once the stock data is fetched, you will be redirected to a new page showing the stock name and the charts.

2. Scroll down to view the charts.

3. The Candlestick chart displays the open, high, low, and close prices of the stock over the selected time period.

4. The Bar chart displays the volume of the stock traded over the selected time period.

5. The Line chart displays the closing price of the stock over the selected time period.

6. You can interact with the charts by zooming in/out, panning, and hovering over data points for more information.

## Dependencies <a name="dependencies"></a>

The ChatDev Stock Data Application has the following dependencies:

- Flask==2.0.1
- yfinance==0.1.63
- plotly==5.3.1

These dependencies are automatically installed when following the installation instructions.

## Support <a name="support"></a>

For any issues or questions regarding the ChatDev Stock Data Application, please reach out to our support team by email at support@chatdev.com or visit our website at [www.chatdev.com](https://www.chatdev.com).