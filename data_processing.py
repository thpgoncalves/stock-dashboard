import pandas as pd

def calculate_percente_change(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the percentage change of the closing prices.
    """

    data = data.copy()
    data["Percentage Change"] = data["Close"].pct_change() * 100
    return data