import openai
class TechnicalAnalysis:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def prepare_summary(self, latest_close, latest_ema_20, latest_sma_50):
        summary = f"El precio de cierre más reciente de Bitcoin (BTC-USD) es {latest_close:.2f}, con una EMA de 20 días de {latest_ema_20:.2f} y una SMA de 50 días de {latest_sma_50:.2f}. " \
                   "Basado en estos indicadores y considerando las tendencias recientes, volúmenes y otros indicadores relevantes, ¿cuál sería tu recomendación para comprar, vender o mantener Bitcoin? " \
                   "Por favor, proporciona un análisis detallado y una recomendación."
        return summary

    def get_openai_response(self, prompt, summary):
        response = self.client.chat.completions.with_raw_response.create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": summary},
            ],
            model="gpt-4",
        )
        return response.parse()