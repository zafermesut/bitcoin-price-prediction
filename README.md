# Finance Data Analysis

This project provides a web application for analyzing and forecasting financial data using the selected ticker symbol from various markets. Built with Streamlit, it allows users to select a symbol and obtain a one-year analysis and forecast.

## Features

- **Ticker Selection**: Choose from a list of ticker symbols.
- **Data Download**: Fetches historical data using Yahoo Finance.
- **Data Analysis**: Displays closing price trends and seasonal decomposition.
- **Forecasting**: Utilizes the Prophet model to predict future prices.

## How to Use

1. **Select a Ticker Symbol**: Use the dropdown to choose a symbol from the available options.
2. **Review Data**: Click the "Review" button to download and analyze the selected symbol's data.
3. **View Results**: Examine the historical trends and forecast visualizations.

## Technologies Used

- Streamlit
- yfinance
- Prophet
- Plotly
- pandas

## Deployment

The application is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/zafermbilen/bitcoin-price-prediction).
