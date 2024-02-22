import yfinance as yf

# Lista de monedas para verificar
monedas = [
    "mxn", "btc", "eth", "xrp", "ltc", "bch", "tusd", "doge", "chz", "dot",
    "ada", "xlm", "grt", "matic", "avax", "ldo", "paxg", "brl", "ars", "usd",
    "cop", "atom", "trx", "sol", "crv", "lrc", "eur", "snx", "tigres", "axs",
    "bat", "mana", "yfi", "dai", "dydx", "mkr", "sand", "bal", "shib", "uni",
    "aave", "ape", "enj", "algo", "ftm", "omg", "sushi", "comp", "link", "qnt",
    "bar", "usdt", "psg", "pepe", "near", "gala", "arb"
]

# Convertir las monedas a su formato para consulta en Yahoo Finance
# Criptomonedas usualmente necesitan '-USD'. Divisas principales ya tienen su formato.
monedas_yahoo = [f"{moneda.upper()}-USD" if moneda not in ['mxn', 'brl', 'ars', 'usd', 'cop', 'eur'] else moneda.upper()
                 for moneda in monedas]

soportadas = []
no_soportadas = []

for moneda in monedas_yahoo:
    try:
        # Intenta obtener datos de la moneda
        ticker = yf.Ticker(moneda)
        info = ticker.info

        # Verifica si se obtuvo alguna información relevante (marketPrice puede estar en diferentes campos)
        if 'regularMarketPrice' in info and info['regularMarketPrice'] is not None:
            soportadas.append(moneda)
        else:
            no_soportadas.append(moneda)
    except ValueError:
        # Captura específicamente errores de valor, lo que implica problemas al recuperar la información
        no_soportadas.append(moneda)

print("Monedas soportadas por Yahoo Finance:", soportadas)
print("Monedas no soportadas por Yahoo Finance:", no_soportadas)
