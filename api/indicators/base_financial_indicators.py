"""
Comparison of Technical Indicators between Bitso and YahooFinancial:

- SMA_50 (Simple Moving Average of 50 days) shows a minimal difference of 0.20%, indicating a high similarity in the simple moving averages calculated by both sources.
- EMA_20 (Exponential Moving Average of 20 days) also presents a slight discrepancy of 0.21%, reflecting consistency in the exponential moving averages.
- RSI (Relative Strength Index) has a more noticeable variation of 2.95%, which may suggest slight differences in the perceived momentum between the two platforms.
- Bollinger Bands (Upper and Lower) exhibit differences of 0.65% and 0.61% respectively, indicating congruence in the estimated market volatility.
- The MACD Line (Moving Average Convergence Divergence) and Signal Line differ by 3.92% and 0.89% respectively, which could indicate variations in the perception of market momentum and trend.
- VWAP (Volume Weighted Average Price) has a difference of 2.63%, pointing out small discrepancies in the volume-weighted average price.
- Fibonacci Levels (23.6%, 38.2%, 61.8%) show differences of 0.32%, 0.26%, and 0.13% respectively, demonstrating a high coherence in the estimated supports and resistances by both sources.

These percentage differences indicate that, overall, there is a high similarity in the technical indicators provided by Bitso and YahooFinancial, with some minor variations that could be attributed to differences in the input data or the specific calculation methods used by each platform.
"""

class BaseFinancialIndicators:
    """
    This is the base class for financial data processors. It provides the structure and methods
    for downloading and processing financial data, and calculating various technical indicators.

    Attributes:
        symbol (str): The symbol of the asset for which data is to be downloaded.
        start_date (str): The start date for the data range.
        end_date (str): The end date for the data range.
        data (DataFrame): The downloaded and processed financial data.
    """
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
    def fetch_data(self):
        """
        Fetches financial data. This should be implemented by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclass")

    def compute_technical_indicators(self):
        """
        Computes standard technical indicators including 50-day SMA, 20-day EMA, RSI, Bollinger Bands, MACD, VWAP, and Fibonacci Retracement levels.
        """
        self._compute_sma_50()
        self._compute_ema_20()
        self._compute_rsi()
        self._compute_bollinger_bands()
        self._compute_macd()
        self._compute_vwap()
        self._compute_fibonacci_retracement()
    def _compute_sma_50(self):
        """
        Computes the 50-day Simple Moving Average (SMA).
        """
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()

    def _compute_ema_20(self):
        """
        Computes the 20-day Exponential Moving Average (EMA).
        """
        self.data['EMA_20'] = self.data['Close'].ewm(span=20, adjust=False).mean()

    def _compute_rsi(self, period=14):
        """
        Computes the Relative Strength Index (RSI) using a specified period.

        Parameters:
            period (int): Look-back period for RSI calculation. Default is 14 days.
        """
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def _compute_bollinger_bands(self, period=20, num_std_dev=2):
        """
        Computes Bollinger Bands using a specified period and number of standard deviations.

        Parameters:
            period (int): Look-back period for the moving average. Default is 20 days.
            num_std_dev (int): Number of standard deviations for the upper and lower bands. Default is 2.
        """
        ma = self.data['Close'].rolling(window=period).mean()
        std_dev = self.data['Close'].rolling(window=period).std()
        self.data['Bollinger_Upper'] = ma + (std_dev * num_std_dev)
        self.data['Bollinger_Lower'] = ma - (std_dev * num_std_dev)

    def _compute_macd(self, short_period=12, long_period=26):
        """
        Computes the Moving Average Convergence Divergence (MACD) using specified short and long periods.

        Parameters:
            short_period (int): Short period EMA. Default is 12 days.
            long_period (int): Long period EMA. Default is 26 days.
        """
        short_ema = self.data['Close'].ewm(span=short_period, adjust=False).mean()
        long_ema = self.data['Close'].ewm(span=long_period, adjust=False).mean()
        self.data['MACD_Line'] = short_ema - long_ema
        self.data['Signal_Line'] = self.data['MACD_Line'].ewm(span=9, adjust=False).mean()

    def _compute_vwap(self):
        """
        Computes the Volume Weighted Average Price (VWAP).
        """
        cum_vol_price = (self.data['Volume'] * (self.data['High'] + self.data['Low']) / 2).cumsum()
        cum_volume = self.data['Volume'].cumsum()
        self.data['VWAP'] = cum_vol_price / cum_volume

    def _compute_fibonacci_retracement(self):
        """
        Computes Fibonacci Retracement levels.
        """
        high = self.data['High'].max()
        low = self.data['Low'].min()
        diff = high - low
        self.data['Fib_Level_23.6%'] = high - 0.236 * diff
        self.data['Fib_Level_38.2%'] = high - 0.382 * diff
        self.data['Fib_Level_61.8%'] = high - 0.618 * diff

    def get_all_indicator_values(self):
        """
        Retrieves the latest values for all computed technical indicators.

        Returns:
            dict: Latest values of all technical indicators.
        """
        latest_sma_50 = self.data['SMA_50'].iloc[-1]
        latest_ema_20 = self.data['EMA_20'].iloc[-1]
        latest_rsi = self.data['RSI'].iloc[-1]
        latest_bollinger_upper = self.data['Bollinger_Upper'].iloc[-1]
        latest_bollinger_lower = self.data['Bollinger_Lower'].iloc[-1]
        latest_macd_line = self.data['MACD_Line'].iloc[-1]
        latest_signal_line = self.data['Signal_Line'].iloc[-1]
        latest_vwap = self.data['VWAP'].iloc[-1]
        latest_fib_23_6 = self.data['Fib_Level_23.6%'].iloc[-1]
        latest_fib_38_2 = self.data['Fib_Level_38.2%'].iloc[-1]
        latest_fib_61_8 = self.data['Fib_Level_61.8%'].iloc[-1]

        return {
            'SMA_50': latest_sma_50,
            'EMA_20': latest_ema_20,
            'RSI': latest_rsi,
            'Bollinger_Upper': latest_bollinger_upper,
            'Bollinger_Lower': latest_bollinger_lower,
            'MACD_Line': latest_macd_line,
            'Signal_Line': latest_signal_line,
            'VWAP': latest_vwap,
            'Fib_Level_23.6%': latest_fib_23_6,
            'Fib_Level_38.2%': latest_fib_38_2,
            'Fib_Level_61.8%': latest_fib_61_8,
        }

    def get_latest_indicator_values(self):
        """
        Retrieves the latest values for SMA, EMA, and the closing price.

        Returns:
            dict: Latest values of SMA, EMA, and closing price.
        """
        latest_sma = self.data['SMA_50'].iloc[-1]
        latest_ema = self.data['EMA_20'].iloc[-1]
        latest_close = self.data['Close'].iloc[-1]
        return {
            'SMA_50': latest_sma,
            'EMA_20': latest_ema,
            'Close': latest_close
        }