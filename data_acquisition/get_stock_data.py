import yfinance as yf

def get_stock_data(ticker: str, period: str, interval: str):
    """
    Fetches stock data for the given ticket, period and interval
    """
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    return data 