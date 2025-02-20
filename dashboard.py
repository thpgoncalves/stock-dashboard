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

    ticker = st.text_input("Enter the stock ticker:", value="AAPL")

    if ticker:
        data = get_stock_data(ticker)
        data = calculate_percente_change(data)

        # display the latest closing price and its percentage change
        st.write("Last Price:", data["Close"].iloc[-1])
        st.write("Percentage Change:", data["Percentage Change"].iloc[-1])

        # display chart
        chart = create_chart(data)
        st.plotly_chart(chart)

if __name__ == "__main__":
    main()