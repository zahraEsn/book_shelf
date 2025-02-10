import os
import psycopg2
from dotenv import load_dotenv
from contextlib import contextmanager
import logger

# Load environment variables from .env file
load_dotenv()

@contextmanager
def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        yield conn
    except psycopg2.Error as e:
        logger.error(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()

def get_db_cursor():
    """Provides a database cursor for executing queries."""
    with get_db_connection() as conn:
        cur = conn.cursor()
        try:
            yield cur
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            cur.close()
