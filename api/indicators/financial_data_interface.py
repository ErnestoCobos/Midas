# api/indicators/financial_data_interface.py

from abc import ABC, abstractmethod
from pandas import DataFrame
from typing import Dict


class FinancialDataInterface(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def compute_technical_indicators(self):
        pass

    @abstractmethod
    def get_latest_indicator_values(self):
        pass

    @abstractmethod
    def get_all_indicator_values(self) -> Dict[str, float]:
        pass

    @abstractmethod
    def get_raw_data(self) -> DataFrame:
        pass
