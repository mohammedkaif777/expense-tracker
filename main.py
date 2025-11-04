from db_manager import create_table, add_expense, get_all_expenses, get_expense_by_category, get_expense_by_date, get_summary
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

def reports_ui():
    print("\nReport Menu:")
    print("1. Filter by category")
    print("2. Filter by date")
    print("3. Summary report")
    choice = input("Choose: ")

    if(choice=="1"):
        category = input("Enter Category: ")
        data = get_expense_by_category(category)
        print(tabulate(data, headers=["Date", "Category","Amount"], tablefmt="grid"))
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        data = get_expense_by_date(date)
        print(tabulate(data, headers=["Date", "Category", "Amount"], tablefmt="grid"))
    elif choice == "3":
        summary = get_summary()
        print("\nSummary Report")
        print(f"Total Entries: {summary[0]}")
        print(f"Total Spent: {summary[1]:.2f}")
        print(f"Average Expense: {summary[2]:.2f}")
        print(f"Top Spending Category: {summary[3]}")
    else:
        print("Invalid option")

def main():
    create_table()
    print("\nWelcome To Expense-Daily\n")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Reports\n4. Exit")
        choice = input("Choose an Option: ")
        if choice == "1":
            add_expense_ui()
        elif choice == "2":
            view_expenses_ui()
        elif choice == "3":
            reports_ui()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()