import streamlit as st
import plotly.express as px
import pandas as pd

from data_acquisition import *
from data_processing import *

def create_chart(data: pd.DataFrame):
    """
    Creates an interactive line chart for the closing prices.
    """
    fig = px.line(data, x=data.index, y="Close", title="Stock Price Over Time")
    return fig

def main():
    st.title("Stock Dashboard")

    col1, col2 = st.columns(2) # creating columns to put the graphics side by side

    with col1:
        ticker1 = st.text_input("Enter the stock ticker:", value="BERK34.SA")
        period1 = st.text_input("Enter the period (e.g., '1d', '1mo', '1y', 'max'):", value="1d", key="period1")
        interval1 = st.text_input("Enter the interval(e.g., '1m', '5m', '1h', '1d'):", value="1m", key="interval1")

        if ticker1:
            data1 = get_stock_data(ticker1, period1, interval1)
            percent_change1 = calculate_percente_change(data1)

            st.write(f"**{ticker1} Last Price:**", data1["Close"].iloc[-1])
            st.write(f"**{ticker1} Percent Change:**", percent_change1)

            chart1 = create_chart(data1)
            st.plotly_chart(chart1, use_container_width=True)
    
    with col2:
        ticker2 = st.text_input("Enter the stock ticker:", value="IVVB11.SA")
        period2 = st.text_input("Enter the period (e.g., '1d', '1mo', '1y', 'max'):", value="1d", key="period2")
        interval2 = st.text_input("Enter the interval(e.g., '1m', '5m', '1h', '1d'):", value="1m", key="interval2")

        if ticker2:
            data2 = get_stock_data(ticker2, period2, interval2)
            percent_change2 = calculate_percente_change(data2)

            st.write(f"**{ticker2} Last Price:**", data2["Close"].iloc[-1])
            st.write(f"**{ticker2} Percent Change:**", percent_change2)

            chart2 = create_chart(data2)
            st.plotly_chart(chart2, use_container_width=True)

if __name__ == "__main__":
    main()