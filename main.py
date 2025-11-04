from db_manager import (
    create_table,
    add_expense,
    get_all_expenses,
    get_expense_by_category,
    get_expense_by_date,
    get_summary
)

def add_expense_ui():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ") or None
    add_expense(date, category, amount, description)
    print("\n✅ Expense added successfully!")

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

def main():
    create_table()
    print("\nWelcome To Expense-Daily\n")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. View by Date")
        print("5. Summary")
        print("6. Exit")

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
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
