import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import numpy as np
import datetime
st.set_page_config(layout="wide")
# Function to load portfolio data from CSV file
def load_portfolio_data(file_path):
    return pd.read_csv(file_path)
# Function to get unique clients from portfolio data
def get_unique_clients(portfolio_data):
    return portfolio_data['Client'].unique()
# Function to render pie chart for selected client
def render_pie_chart(client_data):
    fig = go.Figure(data=[go.Pie(labels=client_data['Company'], values=client_data['Quantity'])])
    st.plotly_chart(fig)
# Function to download stock data for a given symbol
def download_stock_data(symbol):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=6*30)
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data
# Function to perform risk analysis on stock data
def perform_risk_analysis(stock_data):
    # Calculate historical volatility
    stock_data['Log Returns'] = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
    stock_data['Volatility'] = stock_data['Log Returns'].rolling(window=30).std() * np.sqrt(252)
    # Calculate correlation between assets
    correlation_matrix = stock_data['Log Returns'].rolling(window=30).corr()
    # Identify potential outliers or anomalies
    rolling_mean = stock_data['Close'].rolling(window=30).mean()
    rolling_std = stock_data['Close'].rolling(window=30).std()
    z_scores = (stock_data['Close'] - rolling_mean) / rolling_std
    return stock_data, correlation_matrix, z_scores
# Function to display table of stocks at risk
def display_stocks_at_risk(stock_data, z_scores):
    stock_data['Category'] = z_scores.apply(lambda x: 'RISK' if x>2 else 'NON-RISK')
    st.subheader(stock_data['Category'].iloc[-1])
# Main function
def main():
    # Load portfolio data
    portfolio_data = load_portfolio_data('/home/charan/Downloads/dummy_portfolio_data.csv')
    # Get unique clients
    unique_clients = get_unique_clients(portfolio_data)
    # Select client from dropdown
    selected_client = st.selectbox('Select Client', unique_clients)
    # Filter data for selected client
    client_data = portfolio_data[portfolio_data['Client'] == selected_client]
    # Render pie chart for selected client
    render_pie_chart(client_data)
    # Download stock data for unique companies
    unique_companies = client_data['Company'].unique()
    stock_dataframes = {}
    for company in unique_companies:
        stock_dataframes[company] = download_stock_data(company)
    col1, col2 = st.columns(2)
    # Perform risk analysis on stocks
    cat = []
    for company, stock_data in stock_dataframes.items():
        with col1:
            st.subheader(f"Risk Analysis for {company}")

        stock_data, correlation_matrix, z_scores = perform_risk_analysis(stock_data)
        with col2:
            display_stocks_at_risk(stock_data, z_scores)
        with col1:
            st.write("Historical Volatility:")
            st.line_chart(stock_data['Volatility'])
        #st.write("Correlation Matrix:")
        #st.dataframe(correlation_matrix)
        with col2:
            st.write("Outliers or Anomalies:")
            st.line_chart(z_scores)


        
if __name__ == '__main__':
    main()