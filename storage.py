import sqlite3
import time

conn = sqlite3.connect("alerts.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    symbol TEXT PRIMARY KEY,
    last_ts INTEGER
)
""")
conn.commit()

def can_alert(symbol, cooldown_min=15):
    now = int(time.time())
    row = cur.execute(
        "SELECT last_ts FROM alerts WHERE symbol=?", (symbol,)
    ).fetchone()
    if not row:
        return True
    return (now - row[0]) > cooldown_min * 60

def save_alert(symbol):
    ts = int(time.time())
    cur.execute(
        "INSERT OR REPLACE INTO alerts(symbol, last_ts) VALUES (?, ?)",
        (symbol, ts),
    )
    conn.commit()
