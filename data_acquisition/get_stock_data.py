import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, period: str, interval: str):
    """
    Fetches stock data for the given ticket, period and interval
    """
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    return data 

def get_comparison_data(tickers: str | list[str], period="1mo", interval="1d"):
    """
    Fetch historical data for multiple tickers and normalize to a common start date.
    """
    df = pd.DataFrame()

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            stock_data = stock.history(period=period, interval=interval)['Close']

            if not stock_data.empty:
                df[ticker] = stock_data
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")

    if df.empty:
        return df
    
    # normalizing to a common start date
    df = df.dropna(how="any")
    valid_stocks = df.columns[df.iloc[0] > 0]
    df = df[valid_stocks]

    if df.empty:
        print("No valid stocks found after filtering. Returning empty DataFrame.")
        return pd.DataFrame()
    
    # calculating percent change
    df = ((df / df.iloc[0]) - 1) * 100
    
    return df