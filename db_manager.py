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
                amount REAL NOT NULL,
                description TEXT
                )
        """)
        conn.commit()

def add_expense(date, category, amount, description=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))
        conn.commit()


def get_all_expenses():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, category, amount, description FROM expenses")
        return cursor.fetchall()
    
def get_expense_by_category(category):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, category, amount FROM expenses WHERE category = ?",(category,))
        return cursor.fetchall()
    
def get_expense_by_date(date):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, category, amount FROM expenses WHERE date=?",(date,))
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
        row = cursor.fetchone()
        return {
            "total_entries": row[0],
            "total_spent": row[1],
            "avg_expense": row[2],
            "top_category": row[3]
        }

def update_expense(expense_id, new_date, new_category, new_amount, new_description):
    """Update an expense record by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE expenses
            SET date = ?, category = ?, amount = ?, description = ?
            WHERE id = ?
        """, (new_date, new_category, new_amount, new_description, expense_id))
        conn.commit()
        return cursor.rowcount  # returns how many rows were updated


def delete_expense(expense_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()

def get_expense_by_id(expense_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, category, amount, description FROM expenses WHERE id = ?", (expense_id,))
        return cursor.fetchone()

def update_expense(expense_id, date, category, amount, description):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE expenses
            SET date = ?, category = ?, amount = ?, description = ?
            WHERE id = ?
        """, (date, category, amount, description, expense_id))
        conn.commit()



