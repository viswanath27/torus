# ChatDev - Risk Analysis Application User Manual

## Introduction

Welcome to the Risk Analysis Application developed by ChatDev! This application allows you to perform comprehensive risk analysis on stocks for a selected client. It provides evaluation of historical volatility, correlation between assets, and identifies potential outliers or anomalies in the data.

## Installation

To use the Risk Analysis Application, please follow the steps below to install the necessary dependencies:

1. Install Python: Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install required packages: Open a terminal or command prompt and run the following command to install the required packages:

   ```
   pip install streamlit pandas yfinance plotly
   ```

3. Download the application code: Download the `main.py` file from the ChatDev repository or copy the code provided in the previous response.

## Usage

To use the Risk Analysis Application, follow the steps below:

1. Open a terminal or command prompt and navigate to the directory where you saved the `main.py` file.

2. Run the following command to start the application:

   ```
   streamlit run main.py
   ```

3. The application will start and open in your default web browser.

4. Select the client from the dropdown menu. The list of clients is loaded from the `dummy_portfolio_data.csv` file located at `/home/charan/Downloads/`. If you have a different file or path, make sure to update the `load_portfolio_data` function in the code.

5. After selecting the client, a pie chart will be displayed showing the companies and their quantities for the selected client.

6. The application will download stock data for the unique companies in the selected client's portfolio using the `yfinance` library. The data will cover the past 6 months duration.

7. The application will perform risk analysis on the downloaded stock data, including evaluation of historical volatility, correlation between assets, and identification of potential outliers or anomalies.

8. The results of the risk analysis will be displayed in the application, including line charts for historical volatility and outliers, and a table showing the stocks at risk.

9. Explore the results and make informed decisions based on the risk analysis.

10. You can select a different client from the dropdown menu to perform risk analysis for other clients.

## Conclusion

The Risk Analysis Application developed by ChatDev provides a user-friendly interface to perform comprehensive risk analysis on stocks for selected clients. By following the installation and usage instructions provided in this manual, you can make informed decisions based on historical volatility, correlation between assets, and potential outliers or anomalies in the data.

If you have any questions or need further assistance, please reach out to our support team. Happy risk analysis!