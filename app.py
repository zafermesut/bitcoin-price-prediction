import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

st.title("Finance Data Analysis")
ticker = st.text_input("Enter the ticker symbol (e.g., BTC-USD):")


start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

col1, col2 = st.columns([1, 1])

try:

    review_clicked = col1.button("Review")
    refresh_clicked = col2.button("Refresh")
    if review_clicked:
        data = yf.download(ticker, start=start_date, end=end_date)

        if not data.empty:
            st.write(f"Downloaded data for {ticker}")
            st.dataframe(data)  

            data = data.reset_index()
            data = data[["Date", "Close"]]
            data.columns = ["ds", "y"]

            fig = px.line(data, x='ds', y='y', title=f'{ticker} Closing Price Over Time')
            st.plotly_chart(fig)


            decomposition = seasonal_decompose(data.set_index('ds'), model='additive', period=1)
            fig = decomposition.plot()
            fig.suptitle(f'{ticker} Decomposition')
            fig.set_size_inches(12, 8)
            st.pyplot(fig)


            model = Prophet()
            model.fit(data)
            future = model.make_future_dataframe(periods=365)
            forecast = model.predict(future)
            forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(200)
            predictions = model.predict(forecast)
            fig = plot_plotly(model, predictions)
            fig.update_layout(title=f'{ticker} Forecast')
            st.plotly_chart(fig)
            
        else:
            st.write(f"No data found for {ticker}")
        
    if refresh_clicked:
        st.experimental_rerun()
except Exception as e:
    st.write(f"An error occurred: {e}")



