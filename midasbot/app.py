# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from config import SENTRY_DSN, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

from worker import start_worker_thread


sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import BitcoinPrice

@app.route('/')
def index():
    return 'health check'

if __name__ == '__main__':
    start_worker_thread()
    app.run()
