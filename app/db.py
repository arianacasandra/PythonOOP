import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("operations.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            op_type TEXT,
            params TEXT,
            result TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_operation(op_type: str, params: str, result: str):
    conn = sqlite3.connect("operations.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO operations (op_type, params, result, timestamp) VALUES (?, ?, ?, ?)",
        (op_type, params, str(result), datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()