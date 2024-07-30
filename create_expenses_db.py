import sqlite3

def create_db_and_table():
    # Connect to SQLite3 database (or create it if it doesn't exist)
    conn = sqlite3.connect('expenses.db')
    
    # Create a cursor object
    cur = conn.cursor()
    
    # Create the expenses table if it doesn't exist
    cur.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        description TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    print("Database and table created successfully.")

if __name__ == '__main__':
    create_db_and_table()
