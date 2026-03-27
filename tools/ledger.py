from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent / "ledger.db"


def add_expense(item, amount):

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS expenses (item TEXT, amount INT)"
        )

        conn.execute(
            "INSERT INTO expenses VALUES (?,?)",
            (item, amount)
        )

    return f"Recorded expense: {item} {amount}"
