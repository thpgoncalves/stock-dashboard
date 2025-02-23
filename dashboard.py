import streamlit as st
import plotly.express as px
import pandas as pd

from data_acquisition import *
from data_processing import *

st.set_page_config(layout="wide")

def create_chart(data: pd.DataFrame):
    """
    Creates an interactive line chart for the closing prices.
    """
    fig = px.line(data, x=data.index, y="Close", title="Stock Price Over Time")
    return fig

def main():
    st.title("📊 Stock Dashboard")

    st.markdown("### Select Stock and Parameters")

    col1, col2 = st.columns(2) # creating columns to put the graphics side by side

    with col1:
        st.markdown("#### 📌 Stock 1")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker1 = st.text_input("Enter the stock ticker:", value="BERK34.SA", key="ticker1")
        with input_col2:
            period1 = st.text_input("Enter the period: \n\n(e.g., '1d', '1mo', '1y', 'max')", value="1d", key="period1")
        with input_col3:
            interval1 = st.text_input("Enter the interval: \n\n(e.g., '1m', '5m', '1h', '1d')", value="1m", key="interval1")

        if ticker1:
            data1 = get_stock_data(ticker1, period1, interval1)
            if not data1.empty:
                percent_change1 = calculate_percente_change(data1)
                last_price1 = data1["Close"].iloc[-1]

                st.write(f"**{ticker1} Last Price:** $ {last_price1:.2f}", )
                st.write(f"**{ticker1} Percent Change:** {percent_change1}")

                chart1 = create_chart(data1)
                st.plotly_chart(chart1, use_container_width=True)
            else:
                st.write(f"⚠️ No data available for {ticker1}. Try a different period or interval.")
    
    with col2:
        st.markdown("#### 📌 Stock 2")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker2 = st.text_input("Enter the stock ticker:", value="IVVB11.SA", key="ticker2")
        with input_col2:
            period2 = st.text_input("Enter the period: \n\n(e.g., '1d', '1mo', '1y', 'max')", value="1d", key="period2")
        with input_col3:
            interval2 = st.text_input("Enter the interval: \n\n(e.g., '1m', '5m', '1h', '1d')", value="1m", key="interval2")

        if ticker2:
            data2 = get_stock_data(ticker2, period2, interval2)
            if not data2.empty:   
                percent_change2 = calculate_percente_change(data2)
                last_price2 =  data2["Close"].iloc[-1]

                st.write(f"**{ticker2} Last Price:** $ {last_price2:.2f}",)
                st.write(f"**{ticker2} Percent Change:**", percent_change2)

                chart2 = create_chart(data2)
                st.plotly_chart(chart2, use_container_width=True)
            else:
                st.write(f"⚠️ No data available for {ticker1}. Try a different period or interval.")

if __name__ == "__main__":
    main()