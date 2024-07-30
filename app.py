from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create database and table
def create_db_and_table():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        description TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    with sqlite3.connect('expenses.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM expenses")
        expenses = cur.fetchall()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    with sqlite3.connect('expenses.db') as conn:
        conn.execute("INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)", (date, description, amount))
        conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    with sqlite3.connect('expenses.db') as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_db_and_table()  # Ensure the database and table are created
    app.run(debug=True)
