from expenses.io_manager import load_expenses, save_expenses
from expenses.analytics import show_summary
from expenses.validation import get_valid_amount, get_valid_date
from tabulate import tabulate

def add_expense(expenses):
    category = input("Enter category: ").strip().title()
    amount = get_valid_amount()
    if amount is None: return
    date = get_valid_date()
    if date is None: return
    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    table = [[e["date"], e["category"], e["amount"]] for e in expenses]
    print(tabulate(table, headers=["Date", "Category", "Amount"], tablefmt="grid"))
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spent: ₹{total}")

def main():
    expenses = load_expenses()
    print("Welcome To Expense-Daily")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View Summary\n4. Exit")
        choice = input("Choose an Option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
