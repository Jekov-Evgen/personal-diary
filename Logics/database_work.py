import sqlite3


def connect_to_bd():
    connect = sqlite3.connect("records.db")
    cursor = connect.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS records (
                       id INTEGER PRIMARY KEY,
                       date TEXT NOT NULL,
                       record TEXT NOT NULL
                   )
                   """)
    
    connect.commit()
    connect.close()
    
def insert_to_bd(date, text):
    connect = sqlite3.connect("records.db")
    cursor = connect.cursor()
    
    cursor.execute("""
                   INSERT INTO records(date, record) VALUES (?, ?)
                   """, (date, text))
    
    connect.commit()
    connect.close()
    
def get_data_bd():
    connect = sqlite3.connect("records.db")
    cursor = connect.cursor()
    
    result = cursor.execute("""SELECT * FROM records""").fetchall()
    
    connect.close()
    return result

def del_bd():
    connect = sqlite3.connect("records.db")
    cursor = connect.cursor()
    
    cursor.execute("""DELETE FROM records""")
    
    connect.commit()
    connect.close()