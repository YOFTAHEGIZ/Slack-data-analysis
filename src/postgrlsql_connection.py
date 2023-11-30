# db_connection.py
import os
from sqlalchemy import create_engine

def create_database_engine():
    pg_user = os.environ.get('PG_USER')
    pg_password = os.environ.get('PG_PASSWORD')
    pg_host = os.environ.get('PG_HOST', 'localhost')  
    pg_database = os.environ.get('PG_DATABASE')

    DATABASE_URL = f'postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}'
    return create_engine(DATABASE_URL)