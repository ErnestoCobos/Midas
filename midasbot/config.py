# config.py
import os

POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY', 'default_polygon_api_key')
SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{os.environ.get('MYSQL_DATABASE_USERNAME')}:" 
    f"{os.environ.get('MYSQL_DATABASE_PASSWORD')}@"
    f"{os.environ.get('MYSQL_DATABASE_HOST')}/"
    f"{os.environ.get('MYSQL_DATABASE_DB')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SENTRY_DSN = os.environ.get('SENTRY_DSN', 'default_sentry_dsn_url')
print(SQLALCHEMY_DATABASE_URI)