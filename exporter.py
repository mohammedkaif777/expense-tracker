import csv
import json
from db_manager import get_all_expenses

def export_to_csv(filename="expenses.csv"):
    data = get_all_expenses()
    if not data:
        print("⚠️ No expenses found to export.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        writer.writerows(data)
    print(f"✅ Expenses exported successfully to {filename}")

def export_to_json(filename="expenses.json"):
    data = get_all_expenses()
    if not data:
        print("⚠️ No expenses found to export.")
        return
    formatted = [
        {"date": d[0], "category": d[1], "amount": d[2], "description": d[3]}
        for d in data
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(formatted, file, indent=4)
    print(f"✅ Expenses exported successfully to {filename}")
