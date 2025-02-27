import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf

def create_chart(data: pd.DataFrame, title: str) -> pd.DataFrame:
    """
    Creates an interactive line chart for the closing prices.
    """
    fig = px.line(data, x=data.index, y="Close", title=title)
    return fig

def get_comparison_data(tickers: str | list[str], period="1mo", interval="1d"):
    """
    Fetch historical data for multiple tickers and format comparison
    """
    df = pd.DataFrame()

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            stock_data = stock.history(period=period, interval=interval)['Close']

            if not stock_data.empty:
                stock_data = (stock_data / stock_data.iloc[0] - 1) * 100 # gets percent changes
                df[ticker] = stock_data
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")    
    return df

def plot_comparison_chart(df):
    """
    Generate comparison line chart for multiple stocks.
    """
    if df.empty:
        return None
    
    fig = px.line(
        df, 
        title="Stock Price Comparison", 
        labels={"value": "Percent Change", "variable": "Stock"}
        )
    
    for stock in df.columns:
        last_date = df.index[-1] # last date available
        last_value = df[stock].iloc[-1] # last percent change available

        fig.add_trace(
            go.Scatter(
                x=[last_date],
                y=[last_value],
                text=[f"{last_value:.2f}%"],
                mode="text",
                textposition="middle right",
                showlegend=False
            )
        )
    return fig