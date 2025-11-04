from db_manager import (
    create_table,
    add_expense,
    get_all_expenses,
    get_expense_by_category,
    get_expense_by_date,
    get_summary,
    delete_expense,
    update_expense
)
from validators import get_valid_amount, get_valid_category, get_valid_date
from exporter import export_to_csv, export_to_json


def add_expense_ui():
    print("\n📝 Add Expense")
    date = get_valid_date()
    category = get_valid_category()
    amount = get_valid_amount()
    description = input("Enter description(optional): ").strip()
    add_expense(date, category, amount, description)
    print("✅ Expense added successfully!")

def view_all_expenses():
    expenses = get_all_expenses()
    if not expenses:
        print("\nNo expenses recorded.")
        return
    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"Date: {exp[0]}, Category: {exp[1]}, Amount: ₹{exp[2]}")

def view_by_category():
    category = input("Enter category to filter: ")
    expenses = get_expense_by_category(category)
    if not expenses:
        print(f"\nNo expenses found for category '{category}'.")
        return
    print(f"\n--- Expenses in {category} ---")
    for exp in expenses:
        print(f"Date: {exp[0]}, Amount: ₹{exp[2]}")

def view_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    expenses = get_expense_by_date(date)
    if not expenses:
        print(f"\nNo expenses found for date '{date}'.")
        return
    print(f"\n--- Expenses on {date} ---")
    for exp in expenses:
        print(f"Category: {exp[1]}, Amount: ₹{exp[2]}")

def show_summary():
    summary = get_summary()
    print("\n--- Summary ---")
    print(f"Total Entries: {summary['total_entries']}")
    print(f"Total Spent: ₹{summary['total_spent'] or 0:.2f}")
    print(f"Average Expense: ₹{summary['avg_expense'] or 0:.2f}")
    print(f"Top Category: {summary['top_category'] or 'N/A'}")

def edit_expense_ui():
    expenses = get_all_expenses()
    if not expenses:
        print("\nNo expenses to edit.")
        return

    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp[0]}, Category: {exp[1]}, Amount: ₹{exp[2]}")

    try:
        expense_id = int(input("\nEnter the ID of the expense to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    new_date = input("Enter new date (YYYY-MM-DD): ")
    new_category = input("Enter new category: ")
    try:
        new_amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    new_description = input("Enter new description (optional): ") or None

    updated = update_expense(expense_id, new_date, new_category, new_amount, new_description)
    if updated:
        print("✅ Expense updated successfully.")
    else:
        print("❌ Expense not found.")


def delete_expense_ui():
    expenses = get_all_expenses()
    if not expenses:
        print("\nNo expenses to delete.")
        return

    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp[0]}, Category: {exp[1]}, Amount: ₹{exp[2]}")

    try:
        expense_id = int(input("\nEnter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    deleted = delete_expense(expense_id)
    if deleted:
        print("✅ Expense deleted successfully.")
    else:
        print("❌ Expense not found.")

def main():
    create_table()
    print("\nWelcome To Expense-Daily\n")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. View by Date")
        print("5. Summary")
        print("6. Edit Expense")
        print("7. Delete Expense")
        print("8. Export to CSV")
        print("9. Export to JSON")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense_ui()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            view_by_date()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            edit_expense_ui()
        elif choice == "7":
            delete_expense_ui()
        elif choice == "8":
            export_to_csv()
        elif choice == "9":
            export_to_json()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
