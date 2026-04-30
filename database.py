import psycopg2 
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"), 
        port = os.getenv("DB_PORT"), 
        dbname = os.getenv("DB_NAME"), 
        user= os.getenv("DB_USER"), 
        password= os.getenv("DB_PASSWORD"),
        sslmode= os.getenv("DB_SSLMODE")
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""

    """)
    
    def init_db():
        conn.commit()
        print("Database Ready!")
