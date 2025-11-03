from db_manager import create_table, add_expense, get_all_expenses
from tabulate import tabulate
import logging


def add_expense_ui():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    add_expense(date, category, amount)
    logging.info("Expense added successfully!")

def view_expenses_ui():
    expenses = get_all_expenses()
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print(tabulate(expenses, headers=["Date", "Category", "Amount"], tablefmt="grid"))

def main():
    create_table()
    print("\nWelcome To Expense-Daily\n")
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an Option: ")
        if choice == "1":
            add_expense_ui()
        elif choice == "2":
            view_expenses_ui()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
