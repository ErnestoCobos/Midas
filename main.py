from api.indicators.bitso import Bitso
from analysis.Indicators import Indicators

def print_hi(name):
    # Instancia de Bitso
    bitso_data = Bitso('BTC-MXN', '2023-01-01', '2023-02-20')

    # Instancia de Indicators
    indicators = Indicators(bitso_data)

    # Obtener todos los indicadores
    all_indicators = indicators.get_indicators()

    # Imprimir todos los indicadores
    for indicator, value in all_indicators.items():
        print(f"{indicator}: {value}")


if __name__ == '__main__':
    print_hi('PyCharm')