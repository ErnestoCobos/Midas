import requests
import pandas as pd
from datetime import datetime
from .base_financial_indicators import BaseFinancialIndicators

def get_data(book, currentTimeFrom, currentTimeTo, tf):
    """
    Obtiene datos financieros de la API de Bitso.

    Parámetros:
        book (str): El par de criptomonedas para el que se descargarán los datos.
        currentTimeFrom (int): Timestamp de la fecha de inicio para el rango de datos.
        currentTimeTo (int): Timestamp de la fecha de finalización para el rango de datos.
        tf (int): Intervalo de tiempo en segundos para los datos.

    Retorna:
        dict: Los datos financieros obtenidos de la API de Bitso.
    """
    response = requests.get(
        f"https://bitso.com/api/v3/ohlc?book={book}&time_bucket={tf}&start={currentTimeFrom}&end={currentTimeTo}")
    return response.json()

class Bitso(BaseFinancialIndicators):
    """
    La clase Bitso se utiliza para obtener y procesar datos financieros de Bitso.

    Atributos:
        pair (str): El par de criptomonedas para el que se descargarán los datos.
        start_date (str): Fecha de inicio para el rango de datos.
        end_date (str): Fecha de finalización para el rango de datos.
        tf (int): Intervalo de tiempo en segundos para los datos.
        pageSize (int): Número de elementos por página para la solicitud de datos.
        data (DataFrame): Datos financieros descargados y procesados.

    Métodos:
        fetch_data(): Descarga los datos financieros para el par de criptomonedas especificado y el rango de fechas.
    """
    def __init__(self, pair, start_date, end_date, tf):
        """
        Inicializa la clase Bitso con el par de criptomonedas especificado y el rango de fechas.

        Parámetros:
            pair (str): El par de criptomonedas para el que se descargarán los datos.
            start_date (str): Fecha de inicio para el rango de datos.
            end_date (str): Fecha de finalización para el rango de datos.
            tf (int): Intervalo de tiempo en segundos para los datos.
        """
        super().__init__(pair, start_date, end_date)
        self.tf = tf
        self.pageSize = 1000

    def fetch_data(self):
        """
        Descarga los datos financieros para el par de criptomonedas especificado y el rango de fechas.

        Los datos se obtienen a través de la API de Bitso y se procesan en un DataFrame de pandas.
        """
        start_timestamp = int(datetime.strptime(self.start_date, "%Y-%m-%d").timestamp()) * 1000
        end_timestamp = int(datetime.strptime(self.end_date, "%Y-%m-%d").timestamp()) * 1000

        data = get_data(self.symbol, start_timestamp, end_timestamp, self.tf)
        data_list = []

        if data and data['success']:
            for p in data['payload']:
                line = {'Open': float(p['first_rate']),
                        'High': float(p['max_rate']),
                        'Low': float(p['min_rate']),
                        'Close': float(p['last_rate']),
                        'Adj Close': float(p['last_rate']),  # Duplicating 'Close' as 'Adj Close'
                        'Volume': float(p['volume']),
                        'Date': datetime.fromtimestamp(p['bucket_start_time'] / 1000).strftime('%Y-%m-%d')}
                data_list.append(line)
        else:
            print("Error fetching data", data)

        if data_list:
            df = pd.DataFrame(data_list)
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            self.data = df