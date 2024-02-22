import requests
import pandas as pd
from .base_financial_indicators import BaseFinancialIndicators

class Bitso(BaseFinancialIndicators):
    """
    Downloads and processes financial data from Bitso, including the calculation of various technical indicators.

    Attributes:
        pair (str): Pair of the asset to download data for (e.g., 'btc_mxn').
        start_date (str): Start date for the data range in 'YYYY-MM-DD' format.
        end_date (str): End date for the data range in 'YYYY-MM-DD' format.
        data (DataFrame): Downloaded and processed financial data.
    """

    def __init__(self, pair, start_date, end_date):
        super().__init__(pair, start_date, end_date)

    def fetch_data(self):
        url = f"https://api.bitso.com/v3/ohlcv/?book={self.symbol}&start={self.start_date}&end={self.end_date}&granularity=86400"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["payload"]
            self.data = pd.DataFrame(data)
            self.data['date'] = pd.to_datetime(self.data['time'], unit='s')
            self.data.set_index('date', inplace=True)
            for column in ['open', 'close', 'high', 'low', 'volume']:
                self.data[column] = pd.to_numeric(self.data[column])
        else:
            print("Failed to fetch data")