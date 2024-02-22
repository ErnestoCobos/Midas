from api.indicators.financial_data_interface import FinancialDataInterface

class Indicators:
    """
    The Indicators class is responsible for fetching and processing financial data.

    Attributes:
        data_processor (FinancialDataInterface): An instance of a class that implements the FinancialDataInterface.
    """

    def __init__(self, data_processor: FinancialDataInterface):
        """
        Initializes the Indicators class with a data processor.

        Parameters:
            data_processor (FinancialDataInterface): An instance of a class that implements the FinancialDataInterface.
        """
        self.data_processor = data_processor

    def get_indicators(self):
        """
        Fetches the financial data, computes the technical indicators, and returns the latest values of the indicators.

        Returns:
            dict: A dictionary containing the latest values of the technical indicators.
        """
        self.data_processor.fetch_data()
        self.data_processor.compute_technical_indicators()
        return self.data_processor.get_all_indicator_values()

    def get_raw_data(self):
        """
        Fetches the financial data and returns it in its raw form.

        Returns:
            DataFrame: A DataFrame containing the raw financial data.
        """
        self.data_processor.fetch_data()
        return self.data_processor.get_raw_data()