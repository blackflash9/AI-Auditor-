import sqlite3
from datetime import datetime

DB_NAME = "logistics_audit.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Creating a table for Audit Logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            item_name TEXT,
            declared_value REAL,
            duty_rate REAL,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_audit(item, value, rate, res):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO audits (timestamp, item_name, declared_value, duty_rate, result)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), item, value, rate, res))
    conn.commit()
    conn.close()
    print("✓ Audit saved to local database.")

if __name__ == "__main__":
    init_db()
    print("Database initialized.")

