import streamlit as st
import plotly.express as px
import pandas as pd

from data_acquisition import *
from data_processing import *

st.set_page_config(layout="wide")

def create_chart(data: pd.DataFrame, title: str):
    """
    Creates an interactive line chart for the closing prices.
    """
    fig = px.line(data, x=data.index, y="Close", title=title)
    return fig

def main():
    st.markdown("<h1 style='text-align: center;'>📊 Stock Dashboard</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>  Select Stock and Parameters</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2) # creating columns to put the graphics side by side

    with col1:
        st.markdown(f"####  Stock 1")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker1 = st.text_input("Enter the stock ticker:", value="BERK34.SA", key="ticker1")
        with input_col2:
            period1 = st.text_input("Enter the period: \n\n(e.g., '1d', '1mo', '1y', 'max')", value="1d", key="period1")
        with input_col3:
            interval1 = st.text_input("Enter the interval: \n\n(e.g., '1m', '5m', '1h', '1d')", value="5m", key="interval1")

        if ticker1:
            data1 = get_stock_data(ticker1, period1, interval1)
            if not data1.empty:
                percent_change1 = calculate_percente_change(data1)
                last_price1 = data1["Close"].iloc[-1]

                st.metric(label=f"{ticker1} Last price", value=f"$ {last_price1:.2f}", delta=f"{percent_change1}%")

                chart1 = create_chart(data1, f"{ticker1} Stock Price Over Time")
                st.plotly_chart(chart1, use_container_width=True, key="chart1")
            else:
                st.write(f"⚠️ No data available for {ticker1}. Try a different period or interval.")
    
    with col2:
        st.markdown("####  Stock 2")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker2 = st.text_input("Enter the stock ticker:", value="IVVB11.SA", key="ticker2")
        with input_col2:
            period2 = st.text_input("Enter the period: \n\n(e.g., '1d', '1mo', '1y', 'max')", value="1d", key="period2")
        with input_col3:
            interval2 = st.text_input("Enter the interval: \n\n(e.g., '1m', '5m', '1h', '1d')", value="5m", key="interval2")

        if ticker2:
            data2 = get_stock_data(ticker2, period2, interval2)
            if not data2.empty:   
                percent_change2 = calculate_percente_change(data2)
                last_price2 =  data2["Close"].iloc[-1]
                
                st.metric(label=f"{ticker2} Last price", value=f"$ {last_price2:.2f}", delta=f"{percent_change2}%")                

                chart2 = create_chart(data2, f"{ticker2} Stock Price Over Time")
                st.plotly_chart(chart2, use_container_width=True, key="chart2")
            else:
                st.write(f"⚠️ No data available for {ticker2}. Try a different period or interval.")
    
    # second line with 2 stocks chart
    col3, col4 = st.columns(2) # creating columns to put the graphics side by side

    with col3:
        st.markdown("#### Stock 3")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker3 = st.text_input("Enter the stock ticker:", value="RAIZ4.SA", key="ticker3")
        with input_col2:
            period3 = st.text_input("Enter the period: \n\n (e.g., '1d', '1mo', '1y', 'max')", value='1d', key="period3")
        with input_col3:
            interval3 = st.text_input("Enter the interval: \n\n (e.g., '1m', '5m', '1h', '1d')", value='5m', key="interval3")

        if ticker3:
            data3 = get_stock_data(ticker3, period3, interval3)
            if not data3.empty:
                percent_change3 = calculate_percente_change(data3)
                last_price3 = data3["Close"].iloc[-1]

                st.metric(label=f"{ticker3} Last price", value=f"$ {last_price3:.2f}", delta=f"{percent_change3}%")

                chart3 = create_chart(data3, f"{ticker3} Stock Price Over Time")
                st.plotly_chart(chart3, use_container_width=True, key="chart3")
            else:
                st.write(f"⚠️ No data available for {ticker3}. Try a different period or interval.") 

    with col4:
        st.markdown("#### Stock 3")
        input_col1, input_col2, input_col3 = st.columns([2, 1, 1])

        with input_col1:
            ticker4 = st.text_input("Enter the stock ticker:", value="OPCT3.SA", key="ticker4")
        with input_col2:
            period4 = st.text_input("Enter the period: \n\n (e.g., '1d', '1mo', '1y', 'max')", value='1d', key="period4")
        with input_col3:
            interval4 = st.text_input("Enter the interval: \n\n (e.g., '1m', '5m', '1h', '1d')", value='5m', key="interval4")

        if ticker4:
            data4 = get_stock_data(ticker4, period4, interval4)
            if not data4.empty:
                percent_change4 = calculate_percente_change(data4)
                last_price4 = data4["Close"].iloc[-1]

                st.metric(label=f"{ticker4} Last price", value=f"$ {last_price4:.2f}", delta=f"{percent_change4}%")

                chart4 = create_chart(data4, f"{ticker4} Stock Price Over Time")
                st.plotly_chart(chart4, use_container_width=True, key="chart4")
            else:
                st.write(f"⚠️ No data available for {ticker4}. Try a different period or interval.") 

if __name__ == "__main__":
    main()