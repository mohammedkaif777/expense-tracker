import sqlite3

import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME", "expenses.db")

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        conn.commit()

def add_expense(date, category, amount):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)",
                       (date, category, amount))
        conn.commit()

def get_all_expenses():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, category, amount FROM expenses")
        return cursor.fetchall()
    
def get_expense_by_category(category):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, category, amount FROM expenses WHERE category = ?",(category,))
        return cursor.fetchall()
    
def get_expense_by_date(date):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELET date, category, amount FROM expenses WHERE date=?",(date,))
        return cursor.fetchall()
    
def get_summary():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) AS total_entries,
                SUM(amount) AS total_spent,
                AVG(amount) AS avg_expense,
                (SELECT category FROM expenses GROUP BY category ORDER BY SUM(amount) DESC LIMIT 1) AS top_category
            FROM expenses
        """)
        return cursor.fetchall()
