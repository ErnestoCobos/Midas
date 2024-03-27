# models.py
from app import db
from datetime import datetime

class BitcoinPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    exchange = db.Column(db.Integer)
    conditions = db.Column(db.String(50))  # You might want to process this to a string if it's a list
    participant_timestamp = db.Column(db.BigInteger)
    sip_timestamp = db.Column(db.BigInteger)
    trade_id = db.Column(db.String(50))

    def __repr__(self):
        return f'<BitcoinPrice {self.ticker} {self.price}>'
