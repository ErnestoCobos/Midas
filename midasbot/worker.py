import threading
from time import sleep
from polygon import RESTClient
from extensions import db
from models import BitcoinPrice

def fetch_market_data(api_key):
    with app.app_context():
        client = RESTClient(api_key)
        while True:
            # fetching and processing logic
            sleep(1)

def init_worker(app):
    api_key = app.config['POLYGON_API_KEY']
    thread = threading.Thread(target=lambda: fetch_market_data(api_key, app))
    thread.daemon = True
    thread.start()
