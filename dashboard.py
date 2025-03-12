import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_autorefresh import st_autorefresh

from data_acquisition.get_stock_data import get_stock_data
from data_acquisition.data_search import search_stock
from data_processing.process_stock_data import calculate_percente_change
from data_processing.charts import *

st.set_page_config(layout="wide")

# update the grafics every 60s
st_autorefresh(interval= 60 * 1000, key="data_refresh")

# refresh tester
# if "refresh_count" not in st.session_state:
#     st.session_state.refresh_count = 0

# st.session_state.refresh_count += 1

# st.write(f" **Page refreshed automatically:** '{st.session_state.refresh_count}' times")

# Mapping periods for the buttons
PERIOD_OPTIONS = {
    "Max": ("max", "1d"),
    "YTD": ("ytd", "1d"),
    "Month": ("1mo", "1d"),
    "Week": ("1wk", "1h"),
    "Day": ("1d", "1m"),
    "Custom": ("1y", "1d")
}

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
    
    tab1, tab2 = st.tabs(["📈 Dashboard", "📊 Stock Comparison"])

    with tab1:
        st.markdown("<h1 style='text-align: center;'>Select Stocks Tickers and Parameters</h1>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        for col, stock_number in zip([col1, col2], range(1,3)): # loop for stock 1, 2
            with col:
                st.markdown(f"### Stock {stock_number}")
                
                # default tickers
                default_tickers = ["BERK34.SA", "IVVB11.SA"]
                default_ticker = default_tickers[stock_number - 1]

                # search by name
                company_name = st.text_input(f"Search Stock {stock_number} by Name:", key=f"company_search_{stock_number}", placeholder="Enter company name...")
                selected_stock = None
                if company_name:
                    stock_options = search_stock(company_name)
                    if stock_options:
                        selected_stock = st.selectbox(f"Select Stock {stock_number}:", stock_options, key=f"ticker_selected_{stock_number}") 
                    else:
                        st.warning("No stocks found. Try another search")
                
                # ticker option if user already knows what he wants
                ticker = st.text_input(
                    f"Or enter a ticker manually for Stock {stock_number}",
                    value=selected_stock if selected_stock else default_ticker,
                    key=f"ticker{stock_number}"
                )
                # period selector
                selected_period = st.radio(
                    f"Select period for Stock {stock_number}",
                    options=list(PERIOD_OPTIONS),
                    index=list(PERIOD_OPTIONS.keys()).index("Day"),
                    key=f"period_selection_{stock_number}",
                    horizontal=True
                ) 

                period, interval = PERIOD_OPTIONS[selected_period]
                
                if selected_period == "Custom":
                    period_input = st.text_input("Enter custom period:", placeholder="1d, 1wk, 1mo, 1y, ytd...", key=f"stock_period_{stock_number}")
                    interval_input = st.text_input("Enter custom interval:", placeholder="1m, 1h, 1d, 1wk, 1mo...", key=f"stock_interval_{stock_number}")   

                    period = period_input if period_input else "1y"
                    interval = interval_input if interval_input else "1d"

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
                
                # default tickers
                default_tickers = ["RAIZ4.SA", "OPCT3.SA"]
                default_ticker = default_tickers[stock_number - 3]

                # search by name
                company_name = st.text_input(f"Search Stock {stock_number} by Name:", key=f"company_search_{stock_number}", placeholder="Enter company name...")
                selected_stock = None
                if company_name:
                    stock_options = search_stock(company_name)
                    if stock_options:
                        selected_stock = st.selectbox(f"Select Stock {stock_number}:", stock_options, key=f"ticker_selected_{stock_number}") 
                    else:
                        st.warning("No stocks found. Try another search")
                
                # ticker option if user already knows what he wants
                ticker = st.text_input(
                    f"Or enter ticker manually for Stock {stock_number}:", 
                    value=selected_stock if selected_stock else default_ticker,
                    key=f"ticker{stock_number}"
                    )
                
                # period selector
                selected_period = st.radio(
                    f"Select period for Stock {stock_number}",
                    options=list(PERIOD_OPTIONS),
                    index=list(PERIOD_OPTIONS.keys()).index("Day"),
                    key=f"period_selection_{stock_number}",
                    horizontal=True
                )

                period, interval = PERIOD_OPTIONS[selected_period]
                
                if selected_period == "Custom":
                    period_input = st.text_input("Enter custom period:", placeholder="1d, 1wk, 1mo, 1y, ytd...", key=f"stock_period_{stock_number}")
                    interval_input = st.text_input("Enter custom interval:", placeholder="1m, 1h, 1d, 1wk, 1mo...", key=f"stock_interval_{stock_number}")   
                    
                    period = period_input if period_input else "1y"
                    interval = interval_input if interval_input else "1d"

                if ticker:
                    data = get_stock_data(ticker, period, interval)
                    if not data.empty:
                        percent_change = calculate_percente_change(data)
                        last_price = data["Close"].iloc[-1]

                        st.metric(label=f"{ticker} Last Price", value=f"R$ {last_price:.2f}", delta=f"{percent_change}%")

                        chart = create_chart(data, f"{ticker} Stock Price Over Time")
                        st.plotly_chart(chart, use_container_width=True, key=f"chart{stock_number}")
        
        # If you want to add another line with 2 charts, create the collumns 
        # and repeat the loop changing the range and collumns variable name
    
    # Comparison tab
    with tab2:
        st.markdown("### Compare multiple Stocks")

        # search company by the name
        comparison_company_name = st.text_input("Search Stock by Company Name:", placeholder="Enter the company name...", key="comparison_search")
        
        selected_comparison_stock = None
        if comparison_company_name:
            comparison_stock_options = search_stock(comparison_company_name)
            if comparison_stock_options:
                selected_comparison_stock = st.selectbox("Select Stock:", options=comparison_stock_options, key="comparison_ticker_selected")
            else:
                st.warning("No stocks found. Try another search.")
        
        # allow manual tickers input
        manual_tickers = st.text_area("Enter tickers separated by commas:", "BERK34.SA, IVVB11.SA, RAIZ4.SA, OPCT3.SA") # Change default stocks
        manual_ticker_list = [ticker.strip() for ticker in manual_tickers.split(',') if ticker.split()]

        if selected_comparison_stock and selected_comparison_stock not in manual_ticker_list:
            manual_ticker_list.append(selected_comparison_stock)
        
        # Period selector
        selected_comparison_period = st.radio(
            "Select comparison period:",
            options=list(PERIOD_OPTIONS),
            index = list(PERIOD_OPTIONS.keys()).index("Day"), # default selection
            horizontal=True
        )

        comparison_period, comparison_interval = PERIOD_OPTIONS[selected_comparison_period]
        
        if selected_comparison_period == "Custom":
            comparison_period_input = st.text_input("Enter custom period:", placeholder="1d, 1wk, 1mo, 1y, ytd...", key="custom_comparison_period")
            comparison_interval_input = st.text_input("Enter custom interval:", placeholder="1m, 1h, 1d, 1wk, 1mo...", key="custom_comparison_interval")

            comparison_period = comparison_period_input if comparison_period_input else "1y"
            comparison_interval = comparison_interval_input if comparison_interval_input else "1d"

        st.write(f"**Selected Stocks for Comparison:** {', '.join(manual_ticker_list)}")

        if manual_ticker_list:
            df_comparison = get_comparison_data(manual_ticker_list, comparison_period, comparison_interval)
            if not df_comparison.empty:
                fig_comparison = plot_comparison_chart(df_comparison)
                st.plotly_chart(fig_comparison, use_container_width=True)
            else:
                st.write("No data available for the selected stocks.")
        

if __name__ == "__main__":  
    main()