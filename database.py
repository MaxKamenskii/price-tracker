import sqlite3
import datetime
def init_db():
    conn = sqlite3.connect('prices.db')
    print("Connected!")

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS games (
        game_id integer,
        name text,
        price text,
        checked_at text
    )""")

    conn.commit()
    conn.close()

def add_data(id, name, price):
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO games VALUES ('{id}', '{name}', '{price}', '{datetime.datetime.now()}')")
    print("Command executed")
    conn.commit()
    conn.close()
init_db()


