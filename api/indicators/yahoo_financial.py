import yfinance as yf
from .base_financial_indicators import BaseFinancialIndicators

class YahooFinancial(BaseFinancialIndicators):
    """
    Downloads and processes financial data from Yahoo Finance, including the calculation of various technical indicators.

    Attributes:
        symbol (str): Symbol of the asset to download data for.
        start_date (str): Start date for the data range.
        end_date (str): End date for the data range.
        data (DataFrame): Downloaded and processed financial data.
    """

    def __init__(self, symbol, start_date, end_date):
        """
        Initializes the FinancialDataProcessor with the specified asset symbol and date range.

        Parameters:
            symbol (str): Symbol of the asset to download data for.
            start_date (str): Start date for the data range.
            end_date (str): End date for the data range.
        """
        super().__init__(symbol, start_date, end_date)

    def fetch_data(self):
        """
        Downloads financial data for the specified asset and date range from Yahoo Finance.
        """
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        print(self.data)