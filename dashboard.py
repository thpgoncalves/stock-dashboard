import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_autorefresh import st_autorefresh

from data_acquisition import *
from data_processing import *

st.set_page_config(layout="wide")

# update the grafics every 30 sec
st_autorefresh(interval= 30 * 1000, key="data_refresh")

# refresh tester
# if "refresh_count" not in st.session_state:
#     st.session_state.refresh_count = 0

# st.session_state.refresh_count += 1

# st.write(f" **Page refreshed automatically:** '{st.session_state.refresh_count}' times")

# Mapping periods for the buttons
PERIOD_OPTIONS = {
    "YTD": ("ytd", "1d"),
    "Month": ("1mo", "1d"),
    "Week": ("1wk", "1h"),
    "Day": ("1d", "1h"),
}

def create_chart(data: pd.DataFrame, title: str):
    """
    Creates an interactive line chart for the closing prices.
    """
    fig = px.line(data, x=data.index, y="Close", title=title)
    return fig

def main():
    st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;  /* Reduz o espaçamento superior */
        }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>Select Stocks Tickers and Parameters</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    for col, stock_number in zip([col1, col2], range(1,3)): # loop for stock 1, 2
        with col:
            st.markdown(f"### Stock {stock_number}")
            ticker = st.text_input("Enter the stock ticker:", value="BERK34.SA" if stock_number == 1 else "IVVB11.SA", key=f"ticker{stock_number}")

            # period selector
            selected_period = st.radio(
                f"Select period for Stock {stock_number}",
                options=list(PERIOD_OPTIONS),
                index=list(PERIOD_OPTIONS.keys()).index("Day"),
                key=f"period_selection_{stock_number}",
                horizontal=True
            ) 

            period, interval = PERIOD_OPTIONS[selected_period]

            if ticker:
                data = get_stock_data(ticker, period, interval)
                if not data.empty:
                    percent_change = calculate_percente_change(data)
                    last_price = data["Close"].iloc[-1]

                    st.metric(label=f"📈 {ticker} Last Price", value=f"R$ {last_price:.2f}", delta=f"{percent_change}%")

                    chart = create_chart(data, f"{ticker} Stock Price Over Time")
                    st.plotly_chart(chart, use_container_width=True, key=f"chart{stock_number}")

    col3, col4 = st.columns(2)

    for col, stock_number in zip([col3, col4], range(3,5)): # loop for stocks 3, 4
        with col:
            st.markdown(f"### Stock {stock_number}")
            ticker = st.text_input("Enter the stock ticker:", value="RAIZ4.SA" if stock_number == 3 else "OPCT3.SA", key=f"ticker{stock_number}")

            # period selector
            selected_period = st.radio(
                f"Select period for Stock {stock_number}",
                options=list(PERIOD_OPTIONS),
                index=list(PERIOD_OPTIONS.keys()).index("Day"),
                key=f"period_selection_{stock_number}",
                horizontal=True
            ) 

            period, interval = PERIOD_OPTIONS[selected_period]

            if ticker:
                data = get_stock_data(ticker, period, interval)
                if not data.empty:
                    percent_change = calculate_percente_change(data)
                    last_price = data["Close"].iloc[-1]

                    st.metric(label=f"{ticker} Last Price", value=f"R$ {last_price:.2f}", delta=f"{percent_change}%")

                    chart = create_chart(data, f"{ticker} Stock Price Over Time")
                    st.plotly_chart(chart, use_container_width=True, key=f"chart{stock_number}")
if __name__ == "__main__":
    main()