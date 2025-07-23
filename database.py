import mysql.connector

from dotenv import load_dotenv
import os
load_dotenv()

def get_connection():
    db = mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'))

    return db

    # db.close()