import pandas as pd


def calculate_percente_change(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the percentage change of the closing prices.
    """

    data = data.copy()

    percent_change = (
        (data["Close"].iloc[-1] - data["Open"].iloc[0]) / data["Open"].iloc[0]
    ) * 100

    return f"{percent_change:.2f}"
