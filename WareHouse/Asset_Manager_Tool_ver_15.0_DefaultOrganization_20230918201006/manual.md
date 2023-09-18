# ChatDev Stock Data Web Application User Manual

## Introduction

Welcome to the user manual for the ChatDev Stock Data Web Application. This application allows you to retrieve and visualize stock data for a given organization using the Yfinance library in Python. The web application provides candlestick, bar, and line charts to visualize the stock data.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Starting the Application](#starting-the-application)
   - [Entering Stock Name](#entering-stock-name)
   - [Viewing Stock Data](#viewing-stock-data)
3. [Dependencies](#dependencies)
4. [Troubleshooting](#troubleshooting)
5. [Feedback and Support](#feedback-and-support)

## Installation

To use the ChatDev Stock Data Web Application, you need to follow these installation steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:

   ```
   git clone <repository_url>
   ```

4. Change into the cloned directory:

   ```
   cd <repository_directory>
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application

1. Open a terminal or command prompt and navigate to the directory where you installed the application.

2. Run the following command to start the Flask application:

   ```
   python main.py
   ```

3. The application will start running on a local server. You will see output similar to the following:

   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

4. Open a web browser and enter the following URL:

   ```
   http://127.0.0.1:5000/
   ```

### Entering Stock Name

1. On the home page of the application, you will see a form with a field labeled "Stock Name".

2. Enter the name of the stock you want to retrieve data for. For example, you can enter "Apple" to retrieve stock data for Apple Inc.

3. Click the "Submit" button to submit the form.

### Viewing Stock Data

1. After submitting the form, the application will retrieve the stock data using the Yfinance library.

2. The application will generate candlestick, bar, and line charts to visualize the stock data.

3. The charts will be displayed on the web page along with the stock name.

4. You can interact with the charts, zoom in/out, and explore the stock data using the provided controls.

## Dependencies

The ChatDev Stock Data Web Application relies on the following dependencies:

- Flask: A web framework for Python.
- yfinance: A library for retrieving stock data from Yahoo Finance.
- plotly: A library for creating interactive charts and visualizations.

These dependencies are automatically installed when you follow the installation steps mentioned earlier.

## Troubleshooting

If you encounter any issues while using the ChatDev Stock Data Web Application, please try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies correctly. Refer to the installation steps mentioned earlier.

2. Check if there are any error messages displayed in the terminal or command prompt where you started the application. These error messages can provide valuable information about the issue.

3. If the application fails to start or crashes, try restarting your computer and then follow the installation and usage steps again.

4. If the issue persists, please contact our support team for further assistance. See the "Feedback and Support" section for more information.

## Feedback and Support

We value your feedback and are here to provide support for any issues you may encounter while using the ChatDev Stock Data Web Application.

- For general inquiries or feedback, you can reach out to us at [support@chatdev.com](mailto:support@chatdev.com).

- If you encounter any technical issues or need assistance, please fill out the support form at [https://www.chatdev.com/support](https://www.chatdev.com/support). Our support team will get back to you as soon as possible.

Thank you for using the ChatDev Stock Data Web Application! We hope you find it useful for visualizing stock data and making informed investment decisions.