import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
import redis

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

parsed_url = urlparse(DATABASE_URL)
DB_CONFIG = {
    "database": parsed_url.path[1:],  # Remove leading '/'
    "user": parsed_url.username,
    "password": parsed_url.password,
    "host": parsed_url.hostname,
    "port": parsed_url.port,
}

# Connection pool 
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    **DB_CONFIG,
    options="-c statement_timeout=5s"  # timeout
)


def get_db_connection():
    """get connection from pool"""
    try:
        conn = connection_pool.getconn()
        # Verify connection is alive
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        return conn
    except Exception as e:
        print(f"Connection check failed: {e}")
        raise

def get_redis_client():
    return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def return_db_connection(conn):
    """Return connection to the pool"""
    connection_pool.putconn(conn)


# Flask Configuration Class
class Config:
    """Flask application configuration"""
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

    # Server settings
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))

    # Database settings - reuse the same settings for Flask if needed
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
