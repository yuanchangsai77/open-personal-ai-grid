import sqlite3

def add_expense(item, amount):

    conn = sqlite3.connect("ledger.db")

    conn.execute(
        "CREATE TABLE IF NOT EXISTS expenses (item TEXT, amount INT)"
    )

    conn.execute(
        "INSERT INTO expenses VALUES (?,?)",
        (item, amount)
    )

    conn.commit()

    return f"Recorded expense: {item} {amount}"