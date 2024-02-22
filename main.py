from api.indicators.bitso import Bitso
from api.indicators.yahoo_financial import YahooFinancial
from analysis.Indicators import Indicators


def print_hi(name):
    # Bitso instance
    bitso_data = Bitso('btc_usd', '2023-01-01', '2023-02-20', 86400)

    # YahooFinancial instance
    yahoo_data = YahooFinancial('BTC-USD', '2023-01-01', '2023-02-20')

    # Indicators instance for Bitso
    indicators_bitso = Indicators(bitso_data)

    # Indicators instance for YahooFinancial
    indicators_yahoo = Indicators(yahoo_data)

    # Get all indicators for Bitso
    all_indicators_bitso = indicators_bitso.get_indicators()

    # Get all indicators for YahooFinancial
    all_indicators_yahoo = indicators_yahoo.get_indicators()

    # Print all indicators for Bitso
    print("Indicators for Bitso:")
    for indicator, value in all_indicators_bitso.items():
        print(f"{indicator}: {value}")

    # Print all indicators for YahooFinancial
    print("Indicators for YahooFinancial:")
    for indicator, value in all_indicators_yahoo.items():
        print(f"{indicator}: {value}")


if __name__ == '__main__':
    print_hi('PyCharm')
