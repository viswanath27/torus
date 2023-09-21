import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
# Set page layout to wide
st.set_page_config(layout="wide")
# Function to download historical stock data
def download_stock_data(stock_name, start_date, end_date):
    stock_data = yf.download(stock_name, start=start_date, end=end_date)
    # stock_data = stock_data[(stock_data.index >= start_date) & (stock_data.index <= end_date)]
    return stock_data
# Function to render candlestick chart
def render_candlestick_chart(stock_data):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])
    fig.update_layout(title='Candlestick Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render bar chart
def render_bar_chart(stock_data):
    fig = go.Figure(data=[go.Bar(x=stock_data.index, y=stock_data['Volume'])])
    fig.update_layout(title='Bar Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render line chart
def render_line_chart(stock_data):
    fig = go.Figure(data=[go.Scatter(x=stock_data.index, y=stock_data['Close'])])
    fig.update_layout(title='Line Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render OHCL chart
def render_ohcl_chart(stock_data):
    fig = go.Figure(data=[go.Ohlc(x=stock_data.index,
                                  open=stock_data['Open'],
                                  high=stock_data['High'],
                                  low=stock_data['Low'],
                                  close=stock_data['Close'])])
    fig.update_layout(title='OHCL Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render moving average chart
def render_moving_average_chart(stock_data, window_size, start_date, end_date):
    # filtered_data = stock_data[(stock_data.index >= start_date) & (stock_data.index <= end_date)]
    filtered_data = stock_data.copy(deep=True)
    filtered_data['MA'] = filtered_data['Close'].rolling(window=window_size).mean()
    fig = go.Figure(data=[
        go.Scatter(x=filtered_data.index, y=filtered_data['Close'], name='Close'),
        go.Scatter(x=filtered_data.index, y=filtered_data['MA'], name='Moving Average')
    ])
    fig.update_layout(title='Moving Average Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render Bollinger Bands
def render_bollinger_bands(stock_data, window_size, start_date, end_date):
    # filtered_data = stock_data[(stock_data.index >= start_date) & (stock_data.index <= end_date)]
    filtered_data = stock_data.copy(deep=True)
    filtered_data['MA'] = filtered_data['Close'].rolling(window=window_size).mean()
    filtered_data['STD'] = filtered_data['Close'].rolling(window=window_size).std()
    filtered_data['Upper'] = filtered_data['MA'] + 2 * filtered_data['STD']
    filtered_data['Lower'] = filtered_data['MA'] - 2 * filtered_data['STD']
    fig = go.Figure(data=[
        go.Scatter(x=filtered_data.index, y=filtered_data['Close'], name='Close'),
        go.Scatter(x=filtered_data.index, y=filtered_data['Upper'], name='Upper Bollinger Band'),
        go.Scatter(x=filtered_data.index, y=filtered_data['Lower'], name='Lower Bollinger Band')
    ])
    fig.update_layout(title='Bollinger Bands')
    st.plotly_chart(fig, use_container_width=True)
# Function to render Relative Strength Index (RSI) Chart
def render_rsi_chart(stock_data):
    delta = stock_data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    fig = go.Figure(data=[go.Scatter(x=stock_data.index, y=rsi)])
    fig.update_layout(title='Relative Strength Index (RSI) Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render Ichimoku Cloud Chart
def render_ichimoku_cloud_chart(stock_data):
    conversion_line_high = stock_data['High'].rolling(window=9).max()
    conversion_line_low = stock_data['Low'].rolling(window=9).min()
    conversion_line = (conversion_line_high + conversion_line_low) / 2
    base_line_high = stock_data['High'].rolling(window=26).max()
    base_line_low = stock_data['Low'].rolling(window=26).min()
    base_line = (base_line_high + base_line_low) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b_high = stock_data['High'].rolling(window=52).max()
    leading_span_b_low = stock_data['Low'].rolling(window=52).min()
    leading_span_b = (leading_span_b_high + leading_span_b_low) / 2
    fig = go.Figure(data=[
        go.Scatter(x=stock_data.index, y=leading_span_a, name='Leading Span A'),
        go.Scatter(x=stock_data.index, y=leading_span_b, name='Leading Span B'),
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Close')
    ])
    fig.update_layout(title='Ichimoku Cloud Chart')
    st.plotly_chart(fig, use_container_width=True)
# Function to render Histogram
def render_histogram(stock_data):
    fig = go.Figure(data=[go.Histogram(x=stock_data['Close'])])
    fig.update_layout(title='Histogram')
    st.plotly_chart(fig, use_container_width=True)
# Main function
def main():
    st.title('Stock Analysis App')
    # User input for stock name
    stock_name = st.text_input('Enter stock name (e.g., Apple)', 'AAPL')
    # User input for date range
    start_date = st.date_input('Enter start date', value=pd.to_datetime('2023-08-01'))
    end_date = st.date_input('Enter end date', value=pd.to_datetime('2023-09-30'))
    # User input for window size
    window_size = st.number_input('Enter window size for moving average and Bollinger Bands', value=20)
    # Download stock data
    stock_data = download_stock_data(stock_name, start_date, end_date)
    # Render charts on button click
    if st.button('Render Charts'):
        # Create 3x3 grid using st.columns
        col1, col2, col3 = st.columns(3)
        with col1:
            render_candlestick_chart(stock_data)
        with col2:
            render_bar_chart(stock_data)
        with col3:
            render_line_chart(stock_data)
        col4, col5, col6 = st.columns(3)
        with col4:
            render_ohcl_chart(stock_data)
        with col5:
            render_moving_average_chart(stock_data, window_size, start_date, end_date)
        with col6:
            render_bollinger_bands(stock_data, window_size, start_date, end_date)
        col7, col8, col9 = st.columns(3)
        with col7:
            render_rsi_chart(stock_data)
        with col8:
            render_ichimoku_cloud_chart(stock_data)
        with col9:
            render_histogram(stock_data)
# Run the main function
if __name__ == '__main__':
    main()