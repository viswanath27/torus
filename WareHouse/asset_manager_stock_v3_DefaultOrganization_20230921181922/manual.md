# ChatDev Stock Analysis App User Manual

## Introduction

Welcome to the ChatDev Stock Analysis App! This application allows you to analyze the historical stock data of a given organization using various charts and indicators. You can visualize the data in the form of candlestick charts, bar charts, line charts, OHCL charts, moving average charts, Bollinger Bands, Relative Strength Index (RSI) charts, Ichimoku Cloud charts, and histograms.

## Installation

To use the ChatDev Stock Analysis App, you need to install the required dependencies. Please follow the steps below:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the ChatDev Stock Analysis App repository from GitHub: [https://github.com/chatdev-org/stock-analysis-app](https://github.com/chatdev-org/stock-analysis-app)

3. Navigate to the cloned repository folder in your terminal or command prompt.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```shell
   python -m venv env
   ```

5. Activate the virtual environment. The command may vary depending on your operating system:

   - For Windows:

     ```shell
     env\Scripts\activate
     ```

   - For macOS and Linux:

     ```shell
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To use the ChatDev Stock Analysis App, follow the steps below:

1. Make sure you have activated the virtual environment (if you created one) by running the appropriate command mentioned in the installation steps.

2. Run the following command to start the application:

   ```shell
   streamlit run main.py
   ```

3. The application will open in your default web browser.

4. Enter the name of the stock you want to analyze in the text input field. For example, you can enter "AAPL" for Apple.

5. Select the start date and end date for the historical data using the date input fields.

6. Enter the window size for the moving average and Bollinger Bands in the number input field.

7. Click the "Render Charts" button to generate the charts.

8. The charts will be displayed in a 3x3 grid layout.

9. You can interact with the charts by zooming in, panning, and hovering over data points.

10. To exit the application, press Ctrl+C in the terminal or command prompt where the application is running.

## Chart Descriptions

The ChatDev Stock Analysis App provides the following charts:

- Candlestick Chart: Visualizes the open, high, low, and close prices of the stock over time.

- Bar Chart: Shows the volume of trading activity for the stock over time.

- Line Chart: Displays the closing price of the stock over time.

- OHCL Chart: Represents the open, high, low, and close prices of the stock as vertical lines.

- Moving Average Chart: Plots the moving average of the closing price of the stock over time.

- Bollinger Bands: Illustrates the Bollinger Bands, which are volatility bands placed above and below the moving average.

- Relative Strength Index (RSI) Chart: Shows the relative strength index of the stock over time, indicating overbought and oversold conditions.

- Ichimoku Cloud Chart: Displays the Ichimoku Cloud, which consists of several lines that provide support and resistance levels.

- Histogram: Represents the distribution of closing prices of the stock.

## Example

Here is an example of how to use the ChatDev Stock Analysis App:

1. Run the application using the steps mentioned in the "Usage" section.

2. Enter "AAPL" in the stock name input field.

3. Select the start date as August 1, 2023, and the end date as September 30, 2023.

4. Enter the window size as 20.

5. Click the "Render Charts" button.

6. The charts will be displayed in the 3x3 grid layout.

7. You can explore the charts by zooming in, panning, and hovering over data points.

8. Analyze the stock data using the different charts and indicators provided.

9. To analyze another stock, repeat the steps above with a different stock name.

## Conclusion

The ChatDev Stock Analysis App provides a convenient way to analyze the historical stock data of any organization. By visualizing the data using various charts and indicators, you can gain insights into the stock's performance and make informed investment decisions. Enjoy using the app and happy analyzing!