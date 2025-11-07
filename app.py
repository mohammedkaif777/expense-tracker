from flask import Flask, render_template, request, redirect, url_for
from db_manager import add_expense, get_all_expenses, delete_expense, get_expense_by_id, update_expense
import csv
import io
from flask import make_response, jsonify
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row  # makes column access by name possible
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        add_expense(date, category, amount, description)
        return redirect(url_for('index'))

    expenses = get_all_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit(expense_id):
    expense = get_expense_by_id(expense_id)
    if not expense:
        return redirect(url_for('index'))

    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        update_expense(expense_id, date, category, amount, description)
        return redirect(url_for('index'))

    return render_template('edit.html', expense=expense)

@app.route('/export/json')
def export_json():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, category, amount, description FROM expenses")
    data = cursor.fetchall()
    conn.close()

    expenses = [
        {"date": d[0], "category": d[1], "amount": d[2], "description": d[3]}
        for d in data
    ]
    return jsonify(expenses)


@app.route('/export/csv')
def export_csv():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, category, amount, description FROM expenses")
    data = cursor.fetchall()
    conn.close()

    # create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Date", "Category", "Amount", "Description"])
    for row in data:
        writer.writerow(row)

    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=expenses.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

@app.route('/summary')
def summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            COUNT(*) AS total_entries,
            SUM(amount) AS total_spent,
            AVG(amount) AS avg_expense,
            (SELECT category FROM expenses GROUP BY category ORDER BY SUM(amount) DESC LIMIT 1) AS top_category
        FROM expenses
    """)
    result = cursor.fetchone()
    conn.close()

    summary_data = {
        "total_entries": result[0] or 0,
        "total_spent": result[1] or 0.0,
        "avg_expense": result[2] or 0.0,
        "top_category": result[3] or "N/A"
    }

    return render_template('summary.html', summary=summary_data)

if __name__ == '__main__':
    app.run(debug=True)
