import yfinance as yf

def get_stock_data(ticker: str):
    """
    Fetches intraday stock data for the given ticket
    """
    data = yf.Ticker(ticker).history(period="5d", interval="1m")
    return data 