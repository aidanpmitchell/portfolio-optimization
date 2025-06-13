import yfinance as yf
import pandas as pd

def get_price_data(tickers, start="2020-01-01"):
    """
    Extracts 'Adj Close' prices for multiple tickers from Yahoo Finance.

    Returns:
    - A DataFrame with dates as index, tickers as columns, and adjusted close prices as values.
    """
    data = yf.download(tickers, start=start, auto_adjust=False)

    adj_close = data['Adj Close']

    return adj_close.dropna()
