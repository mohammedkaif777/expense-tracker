import csv, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR,"../expenses.csv")

def load_expenses():
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["amount"] = float(row["amount"])
                expenses.append(row)
            except ValueError:
                continue
    return expenses

def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        fieldnames = ["date", "category","amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)