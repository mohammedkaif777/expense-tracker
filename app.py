from flask import Flask, render_template, request, redirect, url_for
from db_manager import add_expense, get_all_expenses

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
