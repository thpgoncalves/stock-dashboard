import yfinance as yf

def get_stock_data(ticker: str, period: str, interval: str):
    """
    Fetches intraday stock data for the given ticket
    """
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    return data 