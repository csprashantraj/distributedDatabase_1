import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Function to connect to PostgreSQL using the URL
def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Global connection and cursor
conn = connect_db()
cur = conn.cursor()