import openai
import yfinance as yf
from openai import OpenAI
import os

# Define el símbolo del criptoactivo y el rango de fechas
crypto = 'BTC-USD'
start_date = '2023-01-01'
end_date = '2023-02-20'  # Asegúrate de usar una fecha actual o fija para pruebas

# Descarga los datos
data = yf.download(crypto, start=start_date, end=end_date)

# Calcular las medias móviles SMA de 50 días y EMA de 20 días
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

# Encuentra el último valor de SMA y EMA, junto con el precio de cierre más reciente
latest_sma_50 = data['SMA_50'].iloc[-1]
latest_ema_20 = data['EMA_20'].iloc[-1]
latest_close = data['Close'].iloc[-1]

# Preparar el resumen de los indicadores técnicos para el prompt
summary = f"El precio de cierre más reciente de Bitcoin (BTC-USD) es {latest_close:.2f}, con una EMA de 20 días de {latest_ema_20:.2f} y una SMA de 50 días de {latest_sma_50:.2f}. " \
           "Basado en estos indicadores y considerando las tendencias recientes, volúmenes y otros indicadores relevantes, ¿cuál sería tu recomendación para comprar, vender o mantener Bitcoin? " \
           "Por favor, proporciona un análisis detallado y una recomendación."

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


prompt = """You are a financial analyst with expertise in financial reporting, data analysis, and market research. Your key responsibilities include analyzing financial data, forecasting trends, creating financial models, and providing accurate financial insights to support decision-making processes. You are currently working on quarterly financial forecasting and competitor analysis. You are familiar with financial jargon like NPV, P/E ratio, EBITDA, and you regularly interact with the finance team, senior management, and stakeholders.

Given this background, analyze the recent financial performance and market trends for a cryptocurrency like Bitcoin. Consider the latest SMA and EMA indicators, and provide a comprehensive analysis that includes:
- Interpretation of the SMA and EMA trends.
- Forecasting the potential future movement based on these indicators.
- Any financial models that might support the investment decision in Bitcoin.
- A detailed explanation of the financial terminology used in your analysis.

Your analysis should be analytical, precise, and comprehensive, using detailed financial methodologies and data interpretations. Provide clear definitions and explanations of financial concepts to avoid ambiguity, and include step-by-step financial analysis explaining its business relevance."""

response = client.chat.completions.with_raw_response.create(
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": summary},
    ],
    model="gpt-4",
)

# Imprimir la respuesta
completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
