import requests

def search_stock(company_name: str):
    """
    Search for stock ticker by company name using Yahoo Finance API.
    Returns suggestion ticker for the given company name.
    """
    url=f"https://query2.finance.yahoo.com/v1/finance/search?q={company_name}"
    headers = {"User-agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return [res['symbol'] for res in data.get("quotes", []) if "symbol" in res]
    return []

